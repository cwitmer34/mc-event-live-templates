# Minecraft Event Live Templates for IntelliJ IDEA

This package contains IntelliJ IDEA Live Templates for **108 of the most commonly used Minecraft Spigot/Paper events** for version **1.21.10**.

## What's Included

The templates cover all major event categories:
- **37 Player Events** (join, quit, move, interact, chat, death, etc.)
- **16 Block Events** (break, place, burn, explode, etc.)
- **25 Entity Events** (damage, death, spawn, target, etc.)
- **12 Inventory Events** (click, close, craft, smelt, etc.)
- **13 Server/World Events** (load, save, chunk events, weather, etc.)
- **6 Vehicle Events** (enter, exit, move, damage, etc.)

## Installation Methods

### Method 1: Direct File Copy (Recommended)

1. Locate your IntelliJ IDEA configuration directory:
   - **Windows**: `%USERPROFILE%\.IntelliJIdea<version>\config\templates\`
   - **macOS**: `~/Library/Application Support/JetBrains/IntelliJIdea<version>/templates/`
   - **Linux**: `~/.config/JetBrains/IntelliJIdea<version>/templates/`

2. **Close IntelliJ IDEA** (important!)

3. Copy `MinecraftEvents.xml` to the templates directory

4. Restart IntelliJ IDEA

5. Verify installation:
   - Go to **Settings** → **Editor** → **Live Templates**
   - You should see **"Minecraft Events"** group with all templates

### Method 2: Import via Settings

1. Create a ZIP file containing `MinecraftEvents.xml`

2. In IntelliJ IDEA:
   - Go to **File** → **Manage IDE Settings** → **Import Settings**
   - Select your ZIP file
   - Check **"Live templates"** in the import dialog
   - Click **OK**

3. Restart IntelliJ IDEA

### Method 3: Copy/Paste (Individual Templates)

1. Go to **Settings** → **Editor** → **Live Templates**
2. Create a new group called "Minecraft Events"
3. Open the `MinecraftEvents.xml` file
4. Copy individual `<template>` blocks
5. Right-click the group and paste

## Usage

### Basic Usage

1. In any Java file, start typing the event abbreviation (all lowercase)
2. Press **Tab** to expand the template
3. The cursor will be placed inside the method body, ready for you to write code

### Examples

**Type:** `onplayerjoin` → **Press Tab**
```java
@EventHandler
public void onPlayerJoin(PlayerJoinEvent event) {
    █  // cursor here
}
```

**Type:** `onblockbreak` → **Press Tab**
```java
@EventHandler
public void onBlockBreak(BlockBreakEvent event) {
    █  // cursor here
}
```

**Type:** `onentitydamage` → **Press Tab**
```java
@EventHandler
public void onEntityDamage(EntityDamageEvent event) {
    █  // cursor here
}
```

## Complete Template List

### Player Events (37)
| Abbreviation | Event Class | Description |
|-------------|-------------|-------------|
| `onplayerjoin` | PlayerJoinEvent | Called when a player joins the server |
| `onplayerquit` | PlayerQuitEvent | Called when a player leaves the server |
| `onplayerlogin` | PlayerLoginEvent | Called when a player attempts to login |
| `onplayermove` | PlayerMoveEvent | Called when a player moves |
| `onplayerinteract` | PlayerInteractEvent | Called when a player interacts with an object or air |
| `onplayerinteractentity` | PlayerInteractEntityEvent | Called when a player right clicks an entity |
| `onplayerchat` | PlayerChatEvent | Called when a player sends a chat message |
| `onasyncplayerchat` | AsyncPlayerChatEvent | Async version of PlayerChatEvent |
| `onplayercommandpreprocess` | PlayerCommandPreprocessEvent | Called when a player runs a command |
| `onplayerdeath` | PlayerDeathEvent | Called when a player dies |
| `onplayerrespawn` | PlayerRespawnEvent | Called when a player respawns |
| `onplayerdropitem` | PlayerDropItemEvent | Called when a player drops an item |
| `onplayerpickupitem` | PlayerPickupItemEvent | Called when a player picks up an item |
| `onplayeritemheld` | PlayerItemHeldEvent | Called when a player changes their held item |
| `onplayertogglesneak` | PlayerToggleSneakEvent | Called when a player toggles sneak |
| `onplayertogglesprint` | PlayerToggleSprintEvent | Called when a player toggles sprint |
| `onplayerteleport` | PlayerTeleportEvent | Called when a player teleports |
| `onplayerkick` | PlayerKickEvent | Called when a player is kicked from the server |
| `onplayerbedenter` | PlayerBedEnterEvent | Called when a player enters a bed |
| `onplayerbedleave` | PlayerBedLeaveEvent | Called when a player leaves a bed |
| `onplayergamemodechange` | PlayerGameModeChangeEvent | Called when a player's game mode changes |
| `onplayerexpchange` | PlayerExpChangeEvent | Called when a player's exp changes |
| `onplayerlevelchange` | PlayerLevelChangeEvent | Called when a player's level changes |
| `onplayeritemconsume` | PlayerItemConsumeEvent | Called when a player consumes an item |
| `onplayeritemdamage` | PlayerItemDamageEvent | Called when a player's item takes damage |
| `onplayerfish` | PlayerFishEvent | Called when a player fishes |
| `onplayerbucketempty` | PlayerBucketEmptyEvent | Called when a player empties a bucket |
| `onplayerbucketfill` | PlayerBucketFillEvent | Called when a player fills a bucket |
| `onplayereditbook` | PlayerEditBookEvent | Called when a player edits a book |
| `onplayerchangedworld` | PlayerChangedWorldEvent | Called when a player switches to another world |
| `onplayerportal` | PlayerPortalEvent | Called when a player enters a portal |
| `onplayerresourcepackstatus` | PlayerResourcePackStatusEvent | Called when a player's resource pack status changes |
| `onplayerswaphanditems` | PlayerSwapHandItemsEvent | Called when a player swaps items between hands |
| `onplayerarmorstandmanipulate` | PlayerArmorStandManipulateEvent | Called when a player manipulates an armor stand |
| `onplayerattemptpickupitem` | PlayerAttemptPickupItemEvent | Called when a player attempts to pick up an item |
| `onplayeradvancementdone` | PlayerAdvancementDoneEvent | Called when a player completes an advancement |

### Block Events (16)
| Abbreviation | Event Class | Description |
|-------------|-------------|-------------|
| `onblockbreak` | BlockBreakEvent | Called when a block is broken by a player |
| `onblockplace` | BlockPlaceEvent | Called when a block is placed by a player |
| `onblockdamage` | BlockDamageEvent | Called when a block is damaged by a player |
| `onblockignite` | BlockIgniteEvent | Called when a block is ignited |
| `onblockburn` | BlockBurnEvent | Called when a block burns |
| `onblockexplode` | BlockExplodeEvent | Called when a block explodes |
| `onblockfade` | BlockFadeEvent | Called when a block fades, melts or disappears |
| `onblockform` | BlockFormEvent | Called when a block is formed or spreads |
| `onblockgrow` | BlockGrowEvent | Called when a block grows naturally |
| `onblockspread` | BlockSpreadEvent | Called when a block spreads |
| `onblockphysics` | BlockPhysicsEvent | Called when a block physics check is called |
| `onblockpistonextend` | BlockPistonExtendEvent | Called when a piston extends |
| `onblockpistonretract` | BlockPistonRetractEvent | Called when a piston retracts |
| `onblockredstone` | BlockRedstoneEvent | Called when a redstone current changes |
| `onleavesdecay` | LeavesDecayEvent | Called when leaves decay |
| `onsignchange` | SignChangeEvent | Called when a sign is changed by a player |

### Entity Events (25)
| Abbreviation | Event Class | Description |
|-------------|-------------|-------------|
| `onentitydamage` | EntityDamageEvent | Called when an entity is damaged |
| `onentitydamagebyentity` | EntityDamageByEntityEvent | Called when an entity is damaged by another entity |
| `onentitydeath` | EntityDeathEvent | Called when an entity dies |
| `onentityspawn` | EntitySpawnEvent | Called when an entity is spawned |
| `onentitytarget` | EntityTargetEvent | Called when an entity targets another entity |
| `onentitychangeblock` | EntityChangeBlockEvent | Called when an entity changes a block |
| `onentityexplode` | EntityExplodeEvent | Called when an entity explodes |
| `onentityteleport` | EntityTeleportEvent | Called when an entity teleports |
| `onentitycombust` | EntityCombustEvent | Called when an entity combusts |
| `onentityinteract` | EntityInteractEvent | Called when an entity interacts with an object |
| `onentitypickupitem` | EntityPickupItemEvent | Called when an entity picks up an item |
| `onentityportal` | EntityPortalEvent | Called when an entity attempts to enter a portal |
| `onentityregainhealth` | EntityRegainHealthEvent | Called when an entity regains health |
| `onentityshootbow` | EntityShootBowEvent | Called when a LivingEntity shoots a bow |
| `onentitytame` | EntityTameEvent | Called when an entity is tamed |
| `onentitybreed` | EntityBreedEvent | Called when two entities breed |
| `onprojectilehit` | ProjectileHitEvent | Called when a projectile hits something |
| `onprojectilelaunch` | ProjectileLaunchEvent | Called when a projectile is launched |
| `oncreaturespawn` | CreatureSpawnEvent | Called when a creature is spawned into a world |
| `oncreeperpower` | CreeperPowerEvent | Called when a Creeper is struck by lightning |
| `onentityportalenter` | EntityPortalEnterEvent | Called when an entity enters a portal |
| `onfoodlevelchange` | FoodLevelChangeEvent | Called when a player's food level changes |
| `onpigzap` | PigZapEvent | Called when a pig is zapped |
| `onsheepdye` | SheepDyeEvent | Called when a sheep's wool is dyed |
| `onslimesplit` | SlimeSplitEvent | Called when a slime splits |

### Inventory Events (12)
| Abbreviation | Event Class | Description |
|-------------|-------------|-------------|
| `oninventoryclick` | InventoryClickEvent | Called when a player clicks in an inventory |
| `oninventoryclose` | InventoryCloseEvent | Called when an inventory is closed |
| `oninventoryopen` | InventoryOpenEvent | Called when an inventory is opened |
| `oninventorydrag` | InventoryDragEvent | Called when a player drags an item in an inventory |
| `oninventorymoveitem` | InventoryMoveItemEvent | Called when an item is moved from one inventory to another |
| `oninventorypickupitem` | InventoryPickupItemEvent | Called when a hopper picks up an item |
| `onprepareitemcraft` | PrepareItemCraftEvent | Called when an item is about to be crafted |
| `oncraftitem` | CraftItemEvent | Called when an item is crafted |
| `onprepareanvil` | PrepareAnvilEvent | Called when an item is placed in an anvil |
| `onfurnaceburn` | FurnaceBurnEvent | Called when an item is used as fuel in a furnace |
| `onfurnacesmelt` | FurnaceSmeltEvent | Called when an item is smelted in a furnace |
| `onbrew` | BrewEvent | Called when the brewing of the contents inside the Brewing Stand is complete |

### Server/World Events (13)
| Abbreviation | Event Class | Description |
|-------------|-------------|-------------|
| `onserverload` | ServerLoadEvent | Called when the server is loaded |
| `onpluginenable` | PluginEnableEvent | Called when a plugin is enabled |
| `onplugindisable` | PluginDisableEvent | Called when a plugin is disabled |
| `onworldinit` | WorldInitEvent | Called when a world is initialized |
| `onworldload` | WorldLoadEvent | Called when a world is loaded |
| `onworldunload` | WorldUnloadEvent | Called when a world is unloaded |
| `onworldsave` | WorldSaveEvent | Called when a world is saved |
| `onchunkload` | ChunkLoadEvent | Called when a chunk is loaded |
| `onchunkunload` | ChunkUnloadEvent | Called when a chunk is unloaded |
| `onstructuregrow` | StructureGrowEvent | Called when an organic structure attempts to grow |
| `onweatherchange` | WeatherChangeEvent | Called when the weather changes |
| `onthunderchange` | ThunderChangeEvent | Called when the thunder state changes |
| `onspawnchange` | SpawnChangeEvent | Called when the spawn point of the world changes |

### Vehicle Events (6)
| Abbreviation | Event Class | Description |
|-------------|-------------|-------------|
| `onvehicleenter` | VehicleEnterEvent | Called when an entity enters a vehicle |
| `onvehicleexit` | VehicleExitEvent | Called when an entity exits a vehicle |
| `onvehiclemove` | VehicleMoveEvent | Called when a vehicle moves |
| `onvehicledamage` | VehicleDamageEvent | Called when a vehicle is damaged |
| `onvehicledestroy` | VehicleDestroyEvent | Called when a vehicle is destroyed |
| `onvehiclecreate` | VehicleCreateEvent | Called when a vehicle is created |

## Tips and Best Practices

### 1. Auto-Import
The templates are configured with `toShortenFQNames="true"`, which means IntelliJ will automatically add the necessary imports for the event classes.

### 2. Auto-Format
The templates use `toReformat="true"`, so the code will automatically be formatted according to your code style settings.

### 3. Cursor Placement
The `$END$` marker places your cursor inside the method body, ready for you to implement your event logic.

### 4. Method Naming
All method names follow the pattern `on<EventName>` (e.g., `onPlayerJoin`, `onBlockBreak`). Feel free to customize the XML file if you prefer different naming conventions.

### 5. Event Priorities
If you need to add event priorities, you can manually add them after expansion:
```java
@EventHandler(priority = EventPriority.HIGHEST)
public void onPlayerJoin(PlayerJoinEvent event) {
    // your code
}
```

### 6. Cancellable Events
Many events are cancellable. After expanding the template, you can add:
```java
@EventHandler
public void onBlockBreak(BlockBreakEvent event) {
    event.setCancelled(true);  // Prevent the block from breaking
}
```

## Customization

### Editing Templates
1. Go to **Settings** → **Editor** → **Live Templates**
2. Expand **"Minecraft Events"**
3. Select a template and click **Edit**
4. Modify the template text as needed

### Adding More Events
If you need events not included in this package:
1. Go to the [Paper API Javadocs](https://jd.papermc.io/paper/1.21.10/)
2. Navigate to the event package
3. Create a new template following the same pattern

## Troubleshooting

### Templates Not Showing Up
- Make sure you restarted IntelliJ IDEA after copying the file
- Check that the file is in the correct templates directory
- Verify the file has proper XML syntax

### Templates Not Expanding
- Make sure you're in a Java context
- Try pressing **Ctrl+Space** after typing the abbreviation
- Check that the abbreviation is typed correctly (all lowercase)

### Import Issues
- The templates require the Spigot/Paper API to be in your project dependencies
- Make sure your `pom.xml` or `build.gradle` includes the Paper API dependency

## Version Information

- **IntelliJ IDEA**: Compatible with all modern versions (2020.1+)
- **Minecraft**: Designed for PaperMC 1.21.10
- **API**: Works with Spigot API and Paper API

## Support

For issues or suggestions:
1. Check the IntelliJ IDEA documentation on Live Templates
2. Refer to the [Paper API documentation](https://docs.papermc.io/paper/dev/api/)
3. Visit the [PaperMC Discord](https://discord.gg/papermc) for community support

## License

These templates are provided as-is for use with Minecraft plugin development. Feel free to modify and distribute.

---

**Happy Plugin Development!** 🎮
