A FiveM script licensing system, make your script secure by our new system!

First of all, thanks for your support and for checking-out our new release, to get any support or help about it, join our Discord server -> https://discord.gg/Vfu9qHaryp

**Features**:
- Working by Own license, IP, and resource name type.
- Comes with custom discord bot with lot of features (create, remove, change, list all tokens, and more).
- Discord webhook logging.
- No abuses options, fixes for internet connections bypass and more.
- Open source.

## Discord Bot Usage
```
    under developmnet
```  

## Discord Bot Explain
```
    under developmnet
```  
    
    
    
## FiveM Code Installation
```lua
-- [config.lua:3]
Config.Licence = ""
-- Config.Licence is the generated token you got with the discord bot or manually added into the SQL.


-- [server-side.lua:7]
local type = ""
-- This is the resource type that you're using for, like my resource is dz-banking and I want my resource type to be "bank", I will call the type "bank" and create the license with this name as resource type (with the discord bot).

-- [server-side.lua:9]
if resName ~= "resource-name" then
-- "resource-name" is your resource name that you'll choose, who is gonna use this resource should use this resource name or the script will get stucked.

-- [server-side.lua:23]
PerformHttpRequest("https://your-domain.com/auth.php")
-- This is the api connection, make sure to set your correct domain.

-- [server-side.lua:47]
logging_webhook = "WebHook"
-- "WebHook" is your webhook logging, make sure to set your correct webhook.
```
    
    
    
    
## Discord Bot Code Installation
```under development
```    
    
    
    
    
## SQL Installation
```sql
-- [database.sql]
-- Inject database.sql to your sql query, it'll auto create a database named "security", don't delete or rename it.
```
    
    
    
    
## PHP Installation
```php
// [auth.php]
// Make sure to get xampp installed first of all (https://www.apachefriends.org/download.html).
// After the xampp installation, open the "xampp control-panel" then start "Apache" and "MySQL".
// Copy auth.php to htdocs folder (C:/Program Files/xampp/htdocs - or your path).
// Now to run your code, open localhost/auth.php in your browser and make sure it's not showing errors.
// Great! You're ready.
```


Please note that we are not responsible for leaks or publications if you do not take care of encrypting or obfuscation the script!

Our intention is to get our possible maximum security to your script, but we do not help with encryption or obscuration.
