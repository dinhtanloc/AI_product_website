# Docker init

## Setup DB Migration
```bash
# install dotnet-ef to migrate
docker compose up -d
docker ps # checking version

```

```bash
docker exec -it sqlserver bash
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P <SA_PASSWORDS>

```
```sql
# check databases in sqlserver
SELECT name FROM sys.databases;
GO
# Update system db
USE system;
GO

#Check DB migration
SELECT name FROM sys.tables;
GO

```