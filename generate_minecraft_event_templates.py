#!/usr/bin/env python3
"""
Script to generate IntelliJ Live Templates for Minecraft Spigot/Paper Events
Generates an XML file that can be imported into IntelliJ IDEA
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom

# Comprehensive list of the 100 most commonly used Minecraft events
# Organized by category for clarity
MINECRAFT_EVENTS = {
    # Player Events (Most Common)
    "player": [
        ("PlayerJoinEvent", "Called when a player joins the server"),
        ("PlayerQuitEvent", "Called when a player leaves the server"),
        ("PlayerLoginEvent", "Called when a player attempts to login"),
        ("PlayerMoveEvent", "Called when a player moves"),
        ("PlayerInteractEvent", "Called when a player interacts with an object or air"),
        ("PlayerInteractEntityEvent", "Called when a player right clicks an entity"),
        ("PlayerChatEvent", "Called when a player sends a chat message"),
        ("AsyncPlayerChatEvent", "Async version of PlayerChatEvent"),
        ("PlayerCommandPreprocessEvent", "Called when a player runs a command"),
        ("PlayerDeathEvent", "Called when a player dies"),
        ("PlayerRespawnEvent", "Called when a player respawns"),
        ("PlayerDropItemEvent", "Called when a player drops an item"),
        ("PlayerPickupItemEvent", "Called when a player picks up an item"),
        ("PlayerItemHeldEvent", "Called when a player changes their held item"),
        ("PlayerToggleSneakEvent", "Called when a player toggles sneak"),
        ("PlayerToggleSprintEvent", "Called when a player toggles sprint"),
        ("PlayerTeleportEvent", "Called when a player teleports"),
        ("PlayerKickEvent", "Called when a player is kicked from the server"),
        ("PlayerBedEnterEvent", "Called when a player enters a bed"),
        ("PlayerBedLeaveEvent", "Called when a player leaves a bed"),
        ("PlayerGameModeChangeEvent", "Called when a player's game mode changes"),
        ("PlayerExpChangeEvent", "Called when a player's exp changes"),
        ("PlayerLevelChangeEvent", "Called when a player's level changes"),
        ("PlayerItemConsumeEvent", "Called when a player consumes an item"),
        ("PlayerItemDamageEvent", "Called when a player's item takes damage"),
        ("PlayerFishEvent", "Called when a player fishes"),
        ("PlayerBucketEmptyEvent", "Called when a player empties a bucket"),
        ("PlayerBucketFillEvent", "Called when a player fills a bucket"),
        ("PlayerEditBookEvent", "Called when a player edits a book"),
        ("PlayerChangedWorldEvent", "Called when a player switches to another world"),
        ("PlayerPortalEvent", "Called when a player enters a portal"),
        ("PlayerResourcePackStatusEvent", "Called when a player's resource pack status changes"),
        ("PlayerSwapHandItemsEvent", "Called when a player swaps items between hands"),
        ("PlayerArmorStandManipulateEvent", "Called when a player manipulates an armor stand"),
        ("PlayerAttemptPickupItemEvent", "Called when a player attempts to pick up an item"),
        ("PlayerAdvancementDoneEvent", "Called when a player completes an advancement"),
    ],
    
    # Block Events
    "block": [
        ("BlockBreakEvent", "Called when a block is broken by a player"),
        ("BlockPlaceEvent", "Called when a block is placed by a player"),
        ("BlockDamageEvent", "Called when a block is damaged by a player"),
        ("BlockIgniteEvent", "Called when a block is ignited"),
        ("BlockBurnEvent", "Called when a block burns"),
        ("BlockExplodeEvent", "Called when a block explodes"),
        ("BlockFadeEvent", "Called when a block fades, melts or disappears"),
        ("BlockFormEvent", "Called when a block is formed or spreads"),
        ("BlockGrowEvent", "Called when a block grows naturally"),
        ("BlockSpreadEvent", "Called when a block spreads"),
        ("BlockPhysicsEvent", "Called when a block physics check is called"),
        ("BlockPistonExtendEvent", "Called when a piston extends"),
        ("BlockPistonRetractEvent", "Called when a piston retracts"),
        ("BlockRedstoneEvent", "Called when a redstone current changes"),
        ("LeavesDecayEvent", "Called when leaves decay"),
        ("SignChangeEvent", "Called when a sign is changed by a player"),
    ],
    
    # Entity Events
    "entity": [
        ("EntityDamageEvent", "Called when an entity is damaged"),
        ("EntityDamageByEntityEvent", "Called when an entity is damaged by another entity"),
        ("EntityDeathEvent", "Called when an entity dies"),
        ("EntitySpawnEvent", "Called when an entity is spawned"),
        ("EntityTargetEvent", "Called when an entity targets another entity"),
        ("EntityChangeBlockEvent", "Called when an entity changes a block"),
        ("EntityExplodeEvent", "Called when an entity explodes"),
        ("EntityTeleportEvent", "Called when an entity teleports"),
        ("EntityCombustEvent", "Called when an entity combusts"),
        ("EntityInteractEvent", "Called when an entity interacts with an object"),
        ("EntityPickupItemEvent", "Called when an entity picks up an item"),
        ("EntityPortalEvent", "Called when an entity attempts to enter a portal"),
        ("EntityRegainHealthEvent", "Called when an entity regains health"),
        ("EntityShootBowEvent", "Called when a LivingEntity shoots a bow"),
        ("EntityTameEvent", "Called when an entity is tamed"),
        ("EntityBreedEvent", "Called when two entities breed"),
        ("ProjectileHitEvent", "Called when a projectile hits something"),
        ("ProjectileLaunchEvent", "Called when a projectile is launched"),
        ("CreatureSpawnEvent", "Called when a creature is spawned into a world"),
        ("CreeperPowerEvent", "Called when a Creeper is struck by lightning"),
        ("EntityPortalEnterEvent", "Called when an entity enters a portal"),
        ("FoodLevelChangeEvent", "Called when a player's food level changes"),
        ("PigZapEvent", "Called when a pig is zapped"),
        ("SheepDyeEvent", "Called when a sheep's wool is dyed"),
        ("SlimeSplitEvent", "Called when a slime splits"),
    ],
    
    # Inventory Events
    "inventory": [
        ("InventoryClickEvent", "Called when a player clicks in an inventory"),
        ("InventoryCloseEvent", "Called when an inventory is closed"),
        ("InventoryOpenEvent", "Called when an inventory is opened"),
        ("InventoryDragEvent", "Called when a player drags an item in an inventory"),
        ("InventoryMoveItemEvent", "Called when an item is moved from one inventory to another"),
        ("InventoryPickupItemEvent", "Called when a hopper picks up an item"),
        ("PrepareItemCraftEvent", "Called when an item is about to be crafted"),
        ("CraftItemEvent", "Called when an item is crafted"),
        ("PrepareAnvilEvent", "Called when an item is placed in an anvil"),
        ("FurnaceBurnEvent", "Called when an item is used as fuel in a furnace"),
        ("FurnaceSmeltEvent", "Called when an item is smelted in a furnace"),
        ("BrewEvent", "Called when the brewing of the contents inside the Brewing Stand is complete"),
    ],
    
    # Server/World Events
    "server": [
        ("ServerLoadEvent", "Called when the server is loaded"),
        ("PluginEnableEvent", "Called when a plugin is enabled"),
        ("PluginDisableEvent", "Called when a plugin is disabled"),
        ("WorldInitEvent", "Called when a world is initialized"),
        ("WorldLoadEvent", "Called when a world is loaded"),
        ("WorldUnloadEvent", "Called when a world is unloaded"),
        ("WorldSaveEvent", "Called when a world is saved"),
        ("ChunkLoadEvent", "Called when a chunk is loaded"),
        ("ChunkUnloadEvent", "Called when a chunk is unloaded"),
        ("StructureGrowEvent", "Called when an organic structure attempts to grow"),
        ("WeatherChangeEvent", "Called when the weather changes"),
        ("ThunderChangeEvent", "Called when the thunder state changes"),
        ("SpawnChangeEvent", "Called when the spawn point of the world changes"),
    ],
    
    # Vehicle Events
    "vehicle": [
        ("VehicleEnterEvent", "Called when an entity enters a vehicle"),
        ("VehicleExitEvent", "Called when an entity exits a vehicle"),
        ("VehicleMoveEvent", "Called when a vehicle moves"),
        ("VehicleDamageEvent", "Called when a vehicle is damaged"),
        ("VehicleDestroyEvent", "Called when a vehicle is destroyed"),
        ("VehicleCreateEvent", "Called when a vehicle is created"),
    ],
}


def create_live_template(abbreviation, event_name, description):
    """
    Create a live template element for a Minecraft event
    
    Args:
        abbreviation: The shorthand to type (e.g., "onplayerjoin")
        event_name: The full event class name (e.g., "PlayerJoinEvent")
        description: Description of what the event does
    
    Returns:
        XML Element for the template
    """
    # Template text with $END$ marking cursor position
    # Using actual newline characters - they will be properly encoded by ElementTree
    method_name = event_name.replace('Event', '')
    template_value = f"@EventHandler\npublic void on{method_name}({event_name} event) {{\n    $END$\n}}"
    
    template = ET.Element('template')
    template.set('name', abbreviation)
    template.set('value', template_value)
    template.set('description', description)
    template.set('toReformat', 'true')
    template.set('toShortenFQNames', 'true')
    
    # Set context to Java
    context = ET.SubElement(template, 'context')
    java_option = ET.SubElement(context, 'option')
    java_option.set('name', 'JAVA_CODE')
    java_option.set('value', 'true')
    
    return template


def generate_templates_xml():
    """
    Generate the complete Live Templates XML file
    """
    xml_lines = ['<templateSet group="Minecraft Events">']
    
    # Add all events
    for category, events in MINECRAFT_EVENTS.items():
        for event_name, description in events:
            # Create abbreviation (e.g., PlayerJoinEvent -> onplayerjoin)
            abbreviation = "on" + event_name.replace("Event", "").lower()
            method_name = event_name.replace('Event', '')
            
            # Build template value with actual newlines
            template_value = f"@EventHandler&#10;public void on{method_name}({event_name} event) {{&#10;    $END$&#10;}}"
            
            # Escape XML special characters in description
            description_escaped = description.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
            
            # Build template XML manually to preserve formatting
            xml_lines.append(f'  <template name="{abbreviation}" value="{template_value}" description="{description_escaped}" toReformat="true" toShortenFQNames="true">')
            xml_lines.append('    <context>')
            xml_lines.append('      <option name="JAVA_CODE" value="true"/>')
            xml_lines.append('    </context>')
            xml_lines.append('  </template>')
    
    xml_lines.append('</templateSet>')
    
    return '\n'.join(xml_lines)


def main():
    """
    Main function to generate the templates file
    """
    print("Generating IntelliJ Live Templates for Minecraft Events...")
    print(f"Total events: {sum(len(events) for events in MINECRAFT_EVENTS.values())}")
    
    xml_content = generate_templates_xml()
    
    output_file = "MinecraftEvents.xml"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    print(f"\n✓ Successfully generated {output_file}")
    print(f"\nTo import into IntelliJ IDEA:")
    print("1. Copy MinecraftEvents.xml to your IntelliJ templates directory:")
    print("   - Windows: %USERPROFILE%\\.IntelliJIdea<version>\\config\\templates\\")
    print("   - macOS: ~/Library/Application Support/JetBrains/IntelliJIdea<version>/templates/")
    print("   - Linux: ~/.config/JetBrains/IntelliJIdea<version>/templates/")
    print("2. Restart IntelliJ IDEA")
    print("3. Go to Settings → Editor → Live Templates")
    print("4. You should see 'Minecraft Events' group with all templates")
    print("\nAlternatively, you can:")
    print("1. Go to File → Manage IDE Settings → Import Settings")
    print("2. Create a ZIP file containing MinecraftEvents.xml")
    print("3. Import the ZIP file and select 'Live templates'")
    print("\nUsage:")
    print("- Type the abbreviation (e.g., 'onplayerjoin') and press Tab")
    print("- The full @EventHandler method will be inserted")
    print("- Cursor will be placed inside the method body")


if __name__ == "__main__":
    main()
