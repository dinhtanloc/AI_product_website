# Init source backend using .NET

## Setup DB Migration
```bash
# install dotnet-ef to migrate
dotnet tool install --global dotnet-ef
dotnet ef # checking version

```

```bash
dotnet ef migrations add <Migration file> #dotnet ef migrations add InitUserTable

dotnet ef database update

```