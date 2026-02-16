using DotNetEnv;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.IdentityModel.Tokens;
using System.Text;

using backend.Data;
using backend.Services;
using backend.Models;


Env.Load(Path.Combine(Directory.GetCurrentDirectory(), "../.env"));

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddOpenApi();


// ================= DB =================
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("Default")));


// ================= JWT =================
var jwtKey = builder.Configuration["Jwt:Key"]!;

builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
.AddJwtBearer(options =>
{
    options.TokenValidationParameters = new TokenValidationParameters
    {
        ValidateIssuer = true,
        ValidateAudience = true,
        ValidateLifetime = true,
        ValidateIssuerSigningKey = true,

        ValidIssuer = builder.Configuration["Jwt:Issuer"],
        ValidAudience = builder.Configuration["Jwt:Audience"],
        IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(jwtKey))
    };
});

builder.Services.AddAuthorization();
builder.Services.AddScoped<JwtService>();


var app = builder.Build();

app.UseAuthentication();
app.UseAuthorization();


// ================= TEST ENDPOINT =================
app.MapGet("/secure", () => "You are authenticated!")
    .RequireAuthorization();

app.MapGet("/config", (IConfiguration config) =>
{
    return new
    {
        Db = config.GetConnectionString("Default"),
        JwtKey = config["Jwt:Key"],
        JwtIssuer = config["Jwt:Issuer"],
        Redis = config["Redis:Connection"]
    };
 });
 

app.MapPost("/register", async (AppDbContext db, JwtService jwt, AuthRequest req) =>
{
    var hash = BCrypt.Net.BCrypt.HashPassword(req.Password);

    var user = new User
    {
        Email = req.Email,
        PasswordHash = hash
    };

    db.Users.Add(user);
    await db.SaveChangesAsync();

    return Results.Ok(jwt.GenerateToken(user));
});

app.MapPost("/login", async (AppDbContext db, JwtService jwt, AuthRequest req) =>
{
    var user = await db.Users.FirstOrDefaultAsync(x => x.Email == req.Email);
    if (user == null || !BCrypt.Net.BCrypt.Verify(req.Password, user.PasswordHash))
        return Results.Unauthorized();

    return Results.Ok(jwt.GenerateToken(user));
});

app.Run();
