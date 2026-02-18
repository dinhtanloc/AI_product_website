// Swagger
using Microsoft.OpenApi.Models;

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


// ================= Swagger =================
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(c =>
{
    c.SwaggerDoc("v1", new OpenApiInfo
    {
        Title = "Assistant Management System API",
        Version = "v1"
    });

    c.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme
    {
        Name = "Authorization",
        Type = SecuritySchemeType.Http,
        Scheme = "bearer",
        BearerFormat = "JWT",
        In = ParameterLocation.Header,
        Description = "Bearer {token}"
    });

    c.AddSecurityRequirement(new OpenApiSecurityRequirement
    {
        {
            new OpenApiSecurityScheme
            {
                Reference = new OpenApiReference
                {
                    Type = ReferenceType.SecurityScheme,
                    Id = "Bearer"
                }
            },
            new string[] {}
        }
    });
});


// ================= CORS =================
var frontendUrl = builder.Configuration["FRONTEND_URL"];

builder.Services.AddCors(options =>
{
    options.AddPolicy("FrontendPolicy", policy =>
    {
        policy
            .WithOrigins(frontendUrl!)   // đọc từ .env
            .AllowAnyHeader()
            .AllowAnyMethod()
            .AllowCredentials();
    });
});


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
        IssuerSigningKey = new SymmetricSecurityKey(
            Encoding.UTF8.GetBytes(jwtKey))
    };
    // Add custom error message for JWT errors
    options.Events = new JwtBearerEvents
    {
        OnChallenge = context =>
        {
            context.HandleResponse();
            context.Response.StatusCode = 401;
            context.Response.ContentType = "application/json";
            var result = System.Text.Json.JsonSerializer.Serialize(new { message = "Token không hợp lệ hoặc đã hết hạn" });
            return context.Response.WriteAsync(result);
        }
    };
});

builder.Services.AddAuthorization();
builder.Services.AddScoped<JwtService>();


var app = builder.Build();


app.UseSwagger();
app.UseSwaggerUI();

app.UseCors("FrontendPolicy");   

app.UseAuthentication();
app.UseAuthorization();


// ================= ENDPOINTS =================
app.MapGet("/secure", () => "You are authenticated!")
    .RequireAuthorization()
    .WithTags("Secure");

app.MapGet("/config", (IConfiguration config) =>
{
    return new
    {
        Db = config.GetConnectionString("Default"),
        JwtIssuer = config["Jwt:Issuer"],
        Redis = config["Redis:Connection"]
    };
}).WithTags("Config");


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
}).WithTags("Auth");


app.MapPost("/login", async (AppDbContext db, JwtService jwt, AuthRequest req) =>
{
    var user = await db.Users.FirstOrDefaultAsync(x => x.Email == req.Email);


    if (user == null || !BCrypt.Net.BCrypt.Verify(req.Password, user.PasswordHash))
        return Results.Json(new { message = "Wrong password or email" }, statusCode: 401);

    return Results.Ok(jwt.GenerateToken(user));
}).WithTags("Auth");


app.Run();
