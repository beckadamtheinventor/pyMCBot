from .item import Item


class _Items:
    def __getitem__(self, key):
        return self.ALL[key]

    AIR = \
        Item(0, "minecraft:air", "Air")
    STONE = \
        Item(1, "minecraft:stone", "Stone")
    STONE_1 = \
        Item(1, "minecraft:stone_1", "Granite")
    STONE_2 = \
        Item(1, "minecraft:stone_2", "Polished Granite")
    STONE_3 = \
        Item(1, "minecraft:stone_3", "Diorite")
    STONE_4 = \
        Item(1, "minecraft:stone_4", "Polished Diorite")
    STONE_5 = \
        Item(1, "minecraft:stone_5", "Andesite")
    STONE_6 = \
        Item(1, "minecraft:stone_6", "Polished Andesite")
    GRASS = \
        Item(2, "minecraft:grass", "Grass")
    DIRT = \
        Item(3, "minecraft:dirt", "Dirt")
    DIRT_1 = \
        Item(3, "minecraft:dirt_1", "Coarse Dirt")
    DIRT_2 = \
        Item(3, "minecraft:dirt_2", "Podzol")
    COBBLESTONE = \
        Item(4, "minecraft:cobblestone", "Cobblestone")
    PLANKS = \
        Item(5, "minecraft:planks", "Oak Wood Plank")
    PLANKS_1 = \
        Item(5, "minecraft:planks_1", "Spruce Wood Plank")
    PLANKS_2 = \
        Item(5, "minecraft:planks_2", "Birch Wood Plank")
    PLANKS_3 = \
        Item(5, "minecraft:planks_3", "Jungle Wood Plank")
    PLANKS_4 = \
        Item(5, "minecraft:planks_4", "Acacia Wood Plank")
    PLANKS_5 = \
        Item(5, "minecraft:planks_5", "Dark Oak Wood Plank")
    SAPLING = \
        Item(6, "minecraft:sapling", "Oak Sapling")
    SAPLING_1 = \
        Item(6, "minecraft:sapling_1", "Spruce Sapling")
    SAPLING_2 = \
        Item(6, "minecraft:sapling_2", "Birch Sapling")
    SAPLING_3 = \
        Item(6, "minecraft:sapling_3", "Jungle Sapling")
    SAPLING_4 = \
        Item(6, "minecraft:sapling_4", "Acacia Sapling")
    SAPLING_5 = \
        Item(6, "minecraft:sapling_5", "Dark Oak Sapling")
    BEDROCK = \
        Item(7, "minecraft:bedrock", "Bedrock")
    FLOWING_WATER = \
        Item(8, "minecraft:flowing_water", "Flowing Water")
    WATER = \
        Item(9, "minecraft:water", "Still Water")
    FLOWING_LAVA = \
        Item(10, "minecraft:flowing_lava", "Flowing Lava")
    LAVA = \
        Item(11, "minecraft:lava", "Still Lava")
    SAND = \
        Item(12, "minecraft:sand", "Sand")
    SAND_1 = \
        Item(12, "minecraft:sand_1", "Red Sand")
    GRAVEL = \
        Item(13, "minecraft:gravel", "Gravel")
    GOLD_ORE = \
        Item(14, "minecraft:gold_ore", "Gold Ore")
    IRON_ORE = \
        Item(15, "minecraft:iron_ore", "Iron Ore")
    COAL_ORE = \
        Item(16, "minecraft:coal_ore", "Coal Ore")
    LOG = \
        Item(17, "minecraft:log", "Oak Wood")
    LOG_1 = \
        Item(17, "minecraft:log_1", "Spruce Wood")
    LOG_2 = \
        Item(17, "minecraft:log_2", "Birch Wood")
    LOG_3 = \
        Item(17, "minecraft:log_3", "Jungle Wood")
    LEAVES = \
        Item(18, "minecraft:leaves", "Oak Leaves")
    LEAVES_1 = \
        Item(18, "minecraft:leaves_1", "Spruce Leaves")
    LEAVES_2 = \
        Item(18, "minecraft:leaves_2", "Birch Leaves")
    LEAVES_3 = \
        Item(18, "minecraft:leaves_3", "Jungle Leaves")
    SPONGE = \
        Item(19, "minecraft:sponge", "Sponge")
    SPONGE_1 = \
        Item(19, "minecraft:sponge_1", "Wet Sponge")
    GLASS = \
        Item(20, "minecraft:glass", "Glass")
    LAPIS_ORE = \
        Item(21, "minecraft:lapis_ore", "Lapis Lazuli Ore")
    LAPIS_BLOCK = \
        Item(22, "minecraft:lapis_block", "Lapis Lazuli Block")
    DISPENSER = \
        Item(23, "minecraft:dispenser", "Dispenser")
    SANDSTONE = \
        Item(24, "minecraft:sandstone", "Sandstone")
    SANDSTONE_1 = \
        Item(24, "minecraft:sandstone_1", "Chiseled Sandstone")
    SANDSTONE_2 = \
        Item(24, "minecraft:sandstone_2", "Smooth Sandstone")
    NOTEBLOCK = \
        Item(25, "minecraft:noteblock", "Note Block")
    BED = \
        Item(26, "minecraft:bed", "Bed")
    GOLDEN_RAIL = \
        Item(27, "minecraft:golden_rail", "Powered Rail")
    DETECTOR_RAIL = \
        Item(28, "minecraft:detector_rail", "Detector Rail")
    STICKY_PISTON = \
        Item(29, "minecraft:sticky_piston", "Sticky Piston")
    WEB = \
        Item(30, "minecraft:web", "Cobweb")
    TALLGRASS = \
        Item(31, "minecraft:tallgrass", "Dead Shrub")
    TALLGRASS_1 = \
        Item(31, "minecraft:tallgrass_1", "Grass")
    TALLGRASS_2 = \
        Item(31, "minecraft:tallgrass_2", "Fern")
    DEADBUSH = \
        Item(32, "minecraft:deadbush", "Dead Bush")
    PISTON = \
        Item(33, "minecraft:piston", "Piston")
    PISTON_HEAD = \
        Item(34, "minecraft:piston_head", "Piston Head")
    WOOL = \
        Item(35, "minecraft:wool", "White Wool")
    WOOL_1 = \
        Item(35, "minecraft:wool_1", "Orange Wool")
    WOOL_2 = \
        Item(35, "minecraft:wool_2", "Magenta Wool")
    WOOL_3 = \
        Item(35, "minecraft:wool_3", "Light Blue Wool")
    WOOL_4 = \
        Item(35, "minecraft:wool_4", "Yellow Wool")
    WOOL_5 = \
        Item(35, "minecraft:wool_5", "Lime Wool")
    WOOL_6 = \
        Item(35, "minecraft:wool_6", "Pink Wool")
    WOOL_7 = \
        Item(35, "minecraft:wool_7", "Gray Wool")
    WOOL_8 = \
        Item(35, "minecraft:wool_8", "Light Gray Wool")
    WOOL_9 = \
        Item(35, "minecraft:wool_9", "Cyan Wool")
    WOOL_10 = \
        Item(35, "minecraft:wool_10", "Purple Wool")
    WOOL_11 = \
        Item(35, "minecraft:wool_11", "Blue Wool")
    WOOL_12 = \
        Item(35, "minecraft:wool_12", "Brown Wool")
    WOOL_13 = \
        Item(35, "minecraft:wool_13", "Green Wool")
    WOOL_14 = \
        Item(35, "minecraft:wool_14", "Red Wool")
    WOOL_15 = \
        Item(35, "minecraft:wool_15", "Black Wool")
    YELLOW_FLOWER = \
        Item(37, "minecraft:yellow_flower", "Dandelion")
    RED_FLOWER = \
        Item(38, "minecraft:red_flower", "Poppy")
    RED_FLOWER_1 = \
        Item(38, "minecraft:red_flower_1", "Blue Orchid")
    RED_FLOWER_2 = \
        Item(38, "minecraft:red_flower_2", "Allium")
    RED_FLOWER_3 = \
        Item(38, "minecraft:red_flower_3", "Azure Bluet")
    RED_FLOWER_4 = \
        Item(38, "minecraft:red_flower_4", "Red Tulip")
    RED_FLOWER_5 = \
        Item(38, "minecraft:red_flower_5", "Orange Tulip")
    RED_FLOWER_6 = \
        Item(38, "minecraft:red_flower_6", "White Tulip")
    RED_FLOWER_7 = \
        Item(38, "minecraft:red_flower_7", "Pink Tulip")
    RED_FLOWER_8 = \
        Item(38, "minecraft:red_flower_8", "Oxeye Daisy")
    BROWN_MUSHROOM = \
        Item(39, "minecraft:brown_mushroom", "Brown Mushroom")
    RED_MUSHROOM = \
        Item(40, "minecraft:red_mushroom", "Red Mushroom")
    GOLD_BLOCK = \
        Item(41, "minecraft:gold_block", "Gold Block")
    IRON_BLOCK = \
        Item(42, "minecraft:iron_block", "Iron Block")
    DOUBLE_STONE_SLAB = \
        Item(43, "minecraft:double_stone_slab", "Double Stone Slab")
    DOUBLE_STONE_SLAB_1 = \
        Item(43, "minecraft:double_stone_slab_1", "Double Sandstone Slab")
    DOUBLE_STONE_SLAB_2 = \
        Item(43, "minecraft:double_stone_slab_2", "Double Wooden Slab")
    DOUBLE_STONE_SLAB_3 = \
        Item(43, "minecraft:double_stone_slab_3", "Double Cobblestone Slab")
    DOUBLE_STONE_SLAB_4 = \
        Item(43, "minecraft:double_stone_slab_4", "Double Brick Slab")
    DOUBLE_STONE_SLAB_5 = \
        Item(43, "minecraft:double_stone_slab_5", "Double Stone Brick Slab")
    DOUBLE_STONE_SLAB_6 = \
        Item(43, "minecraft:double_stone_slab_6", "Double Nether Brick Slab")
    DOUBLE_STONE_SLAB_7 = \
        Item(43, "minecraft:double_stone_slab_7", "Double Quartz Slab")
    STONE_SLAB = \
        Item(44, "minecraft:stone_slab", "Stone Slab")
    STONE_SLAB_1 = \
        Item(44, "minecraft:stone_slab_1", "Sandstone Slab")
    STONE_SLAB_2 = \
        Item(44, "minecraft:stone_slab_2", "Wooden Slab")
    STONE_SLAB_3 = \
        Item(44, "minecraft:stone_slab_3", "Cobblestone Slab")
    STONE_SLAB_4 = \
        Item(44, "minecraft:stone_slab_4", "Brick Slab")
    STONE_SLAB_5 = \
        Item(44, "minecraft:stone_slab_5", "Stone Brick Slab")
    STONE_SLAB_6 = \
        Item(44, "minecraft:stone_slab_6", "Nether Brick Slab")
    STONE_SLAB_7 = \
        Item(44, "minecraft:stone_slab_7", "Quartz Slab")
    BRICK_BLOCK = \
        Item(45, "minecraft:brick_block", "Bricks")
    TNT = \
        Item(46, "minecraft:tnt", "TNT")
    BOOKSHELF = \
        Item(47, "minecraft:bookshelf", "Bookshelf")
    MOSSY_COBBLESTONE = \
        Item(48, "minecraft:mossy_cobblestone", "Moss Stone")
    OBSIDIAN = \
        Item(49, "minecraft:obsidian", "Obsidian")
    TORCH = \
        Item(50, "minecraft:torch", "Torch")
    FIRE = \
        Item(51, "minecraft:fire", "Fire")
    MOB_SPAWNER = \
        Item(52, "minecraft:mob_spawner", "Monster Spawner")
    OAK_STAIRS = \
        Item(53, "minecraft:oak_stairs", "Oak Wood Stairs")
    CHEST = \
        Item(54, "minecraft:chest", "Chest")
    REDSTONE_WIRE = \
        Item(55, "minecraft:redstone_wire", "Redstone Wire")
    DIAMOND_ORE = \
        Item(56, "minecraft:diamond_ore", "Diamond Ore")
    DIAMOND_BLOCK = \
        Item(57, "minecraft:diamond_block", "Diamond Block")
    CRAFTING_TABLE = \
        Item(58, "minecraft:crafting_table", "Crafting Table")
    WHEAT = \
        Item(59, "minecraft:wheat", "Wheat Crops")
    FARMLAND = \
        Item(60, "minecraft:farmland", "Farmland")
    FURNACE = \
        Item(61, "minecraft:furnace", "Furnace")
    LIT_FURNACE = \
        Item(62, "minecraft:lit_furnace", "Burning Furnace")
    STANDING_SIGN = \
        Item(63, "minecraft:standing_sign", "Standing Sign Block")
    WOODEN_DOOR = \
        Item(64, "minecraft:wooden_door", "Oak Door Block")
    LADDER = \
        Item(65, "minecraft:ladder", "Ladder")
    RAIL = \
        Item(66, "minecraft:rail", "Rail")
    STONE_STAIRS = \
        Item(67, "minecraft:stone_stairs", "Cobblestone Stairs")
    WALL_SIGN = \
        Item(68, "minecraft:wall_sign", "Wall-mounted Sign Block")
    LEVER = \
        Item(69, "minecraft:lever", "Lever")
    STONE_PRESSURE_PLATE = \
        Item(70, "minecraft:stone_pressure_plate", "Stone Pressure Plate")
    IRON_DOOR = \
        Item(71, "minecraft:iron_door", "Iron Door Block")
    WOODEN_PRESSURE_PLATE = \
        Item(72, "minecraft:wooden_pressure_plate", "Wooden Pressure Plate")
    REDSTONE_ORE = \
        Item(73, "minecraft:redstone_ore", "Redstone Ore")
    LIT_REDSTONE_ORE = \
        Item(74, "minecraft:lit_redstone_ore", "Glowing Redstone Ore")
    UNLIT_REDSTONE_TORCH = \
        Item(75, "minecraft:unlit_redstone_torch", "Redstone Torch (off)")
    REDSTONE_TORCH = \
        Item(76, "minecraft:redstone_torch", "Redstone Torch (on)")
    STONE_BUTTON = \
        Item(77, "minecraft:stone_button", "Stone Button")
    SNOW_LAYER = \
        Item(78, "minecraft:snow_layer", "Snow")
    ICE = \
        Item(79, "minecraft:ice", "Ice")
    SNOW = \
        Item(80, "minecraft:snow", "Snow Block")
    CACTUS = \
        Item(81, "minecraft:cactus", "Cactus")
    CLAY = \
        Item(82, "minecraft:clay", "Clay")
    REEDS = \
        Item(83, "minecraft:reeds", "Sugar Canes")
    JUKEBOX = \
        Item(84, "minecraft:jukebox", "Jukebox")
    FENCE = \
        Item(85, "minecraft:fence", "Oak Fence")
    PUMPKIN = \
        Item(86, "minecraft:pumpkin", "Pumpkin")
    NETHERRACK = \
        Item(87, "minecraft:netherrack", "Netherrack")
    SOUL_SAND = \
        Item(88, "minecraft:soul_sand", "Soul Sand")
    GLOWSTONE = \
        Item(89, "minecraft:glowstone", "Glowstone")
    PORTAL = \
        Item(90, "minecraft:portal", "Nether Portal")
    LIT_PUMPKIN = \
        Item(91, "minecraft:lit_pumpkin", "Jack o'Lantern")
    CAKE = \
        Item(92, "minecraft:cake", "Cake Block")
    UNPOWERED_REPEATER = \
        Item(93, "minecraft:unpowered_repeater", "Redstone Repeater Block (off)")
    POWERED_REPEATER = \
        Item(94, "minecraft:powered_repeater", "Redstone Repeater Block (on)")
    STAINED_GLASS = \
        Item(95, "minecraft:stained_glass", "White Stained Glass")
    STAINED_GLASS_1 = \
        Item(95, "minecraft:stained_glass_1", "Orange Stained Glass")
    STAINED_GLASS_2 = \
        Item(95, "minecraft:stained_glass_2", "Magenta Stained Glass")
    STAINED_GLASS_3 = \
        Item(95, "minecraft:stained_glass_3", "Light Blue Stained Glass")
    STAINED_GLASS_4 = \
        Item(95, "minecraft:stained_glass_4", "Yellow Stained Glass")
    STAINED_GLASS_5 = \
        Item(95, "minecraft:stained_glass_5", "Lime Stained Glass")
    STAINED_GLASS_6 = \
        Item(95, "minecraft:stained_glass_6", "Pink Stained Glass")
    STAINED_GLASS_7 = \
        Item(95, "minecraft:stained_glass_7", "Gray Stained Glass")
    STAINED_GLASS_8 = \
        Item(95, "minecraft:stained_glass_8", "Light Gray Stained Glass")
    STAINED_GLASS_9 = \
        Item(95, "minecraft:stained_glass_9", "Cyan Stained Glass")
    STAINED_GLASS_10 = \
        Item(95, "minecraft:stained_glass_10", "Purple Stained Glass")
    STAINED_GLASS_11 = \
        Item(95, "minecraft:stained_glass_11", "Blue Stained Glass")
    STAINED_GLASS_12 = \
        Item(95, "minecraft:stained_glass_12", "Brown Stained Glass")
    STAINED_GLASS_13 = \
        Item(95, "minecraft:stained_glass_13", "Green Stained Glass")
    STAINED_GLASS_14 = \
        Item(95, "minecraft:stained_glass_14", "Red Stained Glass")
    STAINED_GLASS_15 = \
        Item(95, "minecraft:stained_glass_15", "Black Stained Glass")
    TRAPDOOR = \
        Item(96, "minecraft:trapdoor", "Wooden Trapdoor")
    MONSTER_EGG = \
        Item(97, "minecraft:monster_egg", "Stone Monster Egg")
    MONSTER_EGG_1 = \
        Item(97, "minecraft:monster_egg_1", "Cobblestone Monster Egg")
    MONSTER_EGG_2 = \
        Item(97, "minecraft:monster_egg_2", "Stone Brick Monster Egg")
    MONSTER_EGG_3 = \
        Item(97, "minecraft:monster_egg_3", "Mossy Stone Brick Monster Egg")
    MONSTER_EGG_4 = \
        Item(97, "minecraft:monster_egg_4", "Cracked Stone Brick Monster Egg")
    MONSTER_EGG_5 = \
        Item(97, "minecraft:monster_egg_5", "Chiseled Stone Brick Monster Egg")
    STONEBRICK = \
        Item(98, "minecraft:stonebrick", "Stone Bricks")
    STONEBRICK_1 = \
        Item(98, "minecraft:stonebrick_1", "Mossy Stone Bricks")
    STONEBRICK_2 = \
        Item(98, "minecraft:stonebrick_2", "Cracked Stone Bricks")
    STONEBRICK_3 = \
        Item(98, "minecraft:stonebrick_3", "Chiseled Stone Bricks")
    BROWN_MUSHROOM_BLOCK = \
        Item(99, "minecraft:brown_mushroom_block", "Brown Mushroom Block")
    RED_MUSHROOM_BLOCK = \
        Item(100, "minecraft:red_mushroom_block", "Red Mushroom Block")
    IRON_BARS = \
        Item(101, "minecraft:iron_bars", "Iron Bars")
    GLASS_PANE = \
        Item(102, "minecraft:glass_pane", "Glass Pane")
    MELON_BLOCK = \
        Item(103, "minecraft:melon_block", "Melon Block")
    PUMPKIN_STEM = \
        Item(104, "minecraft:pumpkin_stem", "Pumpkin Stem")
    MELON_STEM = \
        Item(105, "minecraft:melon_stem", "Melon Stem")
    VINE = \
        Item(106, "minecraft:vine", "Vines")
    FENCE_GATE = \
        Item(107, "minecraft:fence_gate", "Oak Fence Gate")
    BRICK_STAIRS = \
        Item(108, "minecraft:brick_stairs", "Brick Stairs")
    STONE_BRICK_STAIRS = \
        Item(109, "minecraft:stone_brick_stairs", "Stone Brick Stairs")
    MYCELIUM = \
        Item(110, "minecraft:mycelium", "Mycelium")
    WATERLILY = \
        Item(111, "minecraft:waterlily", "Lily Pad")
    NETHER_BRICK = \
        Item(112, "minecraft:nether_brick", "Nether Brick")
    NETHER_BRICK_FENCE = \
        Item(113, "minecraft:nether_brick_fence", "Nether Brick Fence")
    NETHER_BRICK_STAIRS = \
        Item(114, "minecraft:nether_brick_stairs", "Nether Brick Stairs")
    NETHER_WART = \
        Item(115, "minecraft:nether_wart", "Nether Wart")
    ENCHANTING_TABLE = \
        Item(116, "minecraft:enchanting_table", "Enchantment Table")
    BREWING_STAND = \
        Item(117, "minecraft:brewing_stand", "Brewing Stand")
    CAULDRON = \
        Item(118, "minecraft:cauldron", "Cauldron")
    END_PORTAL = \
        Item(119, "minecraft:end_portal", "End Portal")
    END_PORTAL_FRAME = \
        Item(120, "minecraft:end_portal_frame", "End Portal Frame")
    END_STONE = \
        Item(121, "minecraft:end_stone", "End Stone")
    DRAGON_EGG = \
        Item(122, "minecraft:dragon_egg", "Dragon Egg")
    REDSTONE_LAMP = \
        Item(123, "minecraft:redstone_lamp", "Redstone Lamp (inactive)")
    LIT_REDSTONE_LAMP = \
        Item(124, "minecraft:lit_redstone_lamp", "Redstone Lamp (active)")
    DOUBLE_WOODEN_SLAB = \
        Item(125, "minecraft:double_wooden_slab", "Double Oak Wood Slab")
    DOUBLE_WOODEN_SLAB_1 = \
        Item(125, "minecraft:double_wooden_slab_1", "Double Spruce Wood Slab")
    DOUBLE_WOODEN_SLAB_2 = \
        Item(125, "minecraft:double_wooden_slab_2", "Double Birch Wood Slab")
    DOUBLE_WOODEN_SLAB_3 = \
        Item(125, "minecraft:double_wooden_slab_3", "Double Jungle Wood Slab")
    DOUBLE_WOODEN_SLAB_4 = \
        Item(125, "minecraft:double_wooden_slab_4", "Double Acacia Wood Slab")
    DOUBLE_WOODEN_SLAB_5 = \
        Item(125, "minecraft:double_wooden_slab_5", "Double Dark Oak Wood Slab")
    WOODEN_SLAB = \
        Item(126, "minecraft:wooden_slab", "Oak Wood Slab")
    WOODEN_SLAB_1 = \
        Item(126, "minecraft:wooden_slab_1", "Spruce Wood Slab")
    WOODEN_SLAB_2 = \
        Item(126, "minecraft:wooden_slab_2", "Birch Wood Slab")
    WOODEN_SLAB_3 = \
        Item(126, "minecraft:wooden_slab_3", "Jungle Wood Slab")
    WOODEN_SLAB_4 = \
        Item(126, "minecraft:wooden_slab_4", "Acacia Wood Slab")
    WOODEN_SLAB_5 = \
        Item(126, "minecraft:wooden_slab_5", "Dark Oak Wood Slab")
    COCOA = \
        Item(127, "minecraft:cocoa", "Cocoa")
    SANDSTONE_STAIRS = \
        Item(128, "minecraft:sandstone_stairs", "Sandstone Stairs")
    EMERALD_ORE = \
        Item(129, "minecraft:emerald_ore", "Emerald Ore")
    ENDER_CHEST = \
        Item(130, "minecraft:ender_chest", "Ender Chest")
    TRIPWIRE_HOOK = \
        Item(131, "minecraft:tripwire_hook", "Tripwire Hook")
    TRIPWIRE_HOOK = \
        Item(132, "minecraft:tripwire_hook", "Tripwire")
    EMERALD_BLOCK = \
        Item(133, "minecraft:emerald_block", "Emerald Block")
    SPRUCE_STAIRS = \
        Item(134, "minecraft:spruce_stairs", "Spruce Wood Stairs")
    BIRCH_STAIRS = \
        Item(135, "minecraft:birch_stairs", "Birch Wood Stairs")
    JUNGLE_STAIRS = \
        Item(136, "minecraft:jungle_stairs", "Jungle Wood Stairs")
    COMMAND_BLOCK = \
        Item(137, "minecraft:command_block", "Command Block")
    BEACON = \
        Item(138, "minecraft:beacon", "Beacon")
    COBBLESTONE_WALL = \
        Item(139, "minecraft:cobblestone_wall", "Cobblestone Wall")
    COBBLESTONE_WALL_1 = \
        Item(139, "minecraft:cobblestone_wall_1", "Mossy Cobblestone Wall")
    FLOWER_POT = \
        Item(140, "minecraft:flower_pot", "Flower Pot")
    CARROTS = \
        Item(141, "minecraft:carrots", "Carrots")
    POTATOES = \
        Item(142, "minecraft:potatoes", "Potatoes")
    WOODEN_BUTTON = \
        Item(143, "minecraft:wooden_button", "Wooden Button")
    SKULL = \
        Item(144, "minecraft:skull", "Mob Head")
    ANVIL = \
        Item(145, "minecraft:anvil", "Anvil")
    TRAPPED_CHEST = \
        Item(146, "minecraft:trapped_chest", "Trapped Chest")
    LIGHT_WEIGHTED_PRESSURE_PLATE = \
        Item(147, "minecraft:light_weighted_pressure_plate", "Weighted Pressure Plate (light)")
    HEAVY_WEIGHTED_PRESSURE_PLATE = \
        Item(148, "minecraft:heavy_weighted_pressure_plate", "Weighted Pressure Plate (heavy)")
    UNPOWERED_COMPARATOR = \
        Item(149, "minecraft:unpowered_comparator", "Redstone Comparator (inactive)")
    POWERED_COMPARATOR = \
        Item(150, "minecraft:powered_comparator", "Redstone Comparator (active)")
    DAYLIGHT_DETECTOR = \
        Item(151, "minecraft:daylight_detector", "Daylight Sensor")
    REDSTONE_BLOCK = \
        Item(152, "minecraft:redstone_block", "Redstone Block")
    QUARTZ_ORE = \
        Item(153, "minecraft:quartz_ore", "Nether Quartz Ore")
    HOPPER = \
        Item(154, "minecraft:hopper", "Hopper")
    QUARTZ_BLOCK = \
        Item(155, "minecraft:quartz_block", "Quartz Block")
    QUARTZ_BLOCK_1 = \
        Item(155, "minecraft:quartz_block_1", "Chiseled Quartz Block")
    QUARTZ_BLOCK_2 = \
        Item(155, "minecraft:quartz_block_2", "Pillar Quartz Block")
    QUARTZ_STAIRS = \
        Item(156, "minecraft:quartz_stairs", "Quartz Stairs")
    ACTIVATOR_RAIL = \
        Item(157, "minecraft:activator_rail", "Activator Rail")
    DROPPER = \
        Item(158, "minecraft:dropper", "Dropper")
    STAINED_HARDENED_CLAY = \
        Item(159, "minecraft:stained_hardened_clay", "White Hardened Clay")
    STAINED_HARDENED_CLAY_1 = \
        Item(159, "minecraft:stained_hardened_clay_1", "Orange Hardened Clay")
    STAINED_HARDENED_CLAY_2 = \
        Item(159, "minecraft:stained_hardened_clay_2", "Magenta Hardened Clay")
    STAINED_HARDENED_CLAY_3 = \
        Item(159, "minecraft:stained_hardened_clay_3", "Light Blue Hardened Clay")
    STAINED_HARDENED_CLAY_4 = \
        Item(159, "minecraft:stained_hardened_clay_4", "Yellow Hardened Clay")
    STAINED_HARDENED_CLAY_5 = \
        Item(159, "minecraft:stained_hardened_clay_5", "Lime Hardened Clay")
    STAINED_HARDENED_CLAY_6 = \
        Item(159, "minecraft:stained_hardened_clay_6", "Pink Hardened Clay")
    STAINED_HARDENED_CLAY_7 = \
        Item(159, "minecraft:stained_hardened_clay_7", "Gray Hardened Clay")
    STAINED_HARDENED_CLAY_8 = \
        Item(159, "minecraft:stained_hardened_clay_8", "Light Gray Hardened Clay")
    STAINED_HARDENED_CLAY_9 = \
        Item(159, "minecraft:stained_hardened_clay_9", "Cyan Hardened Clay")
    STAINED_HARDENED_CLAY_10 = \
        Item(159, "minecraft:stained_hardened_clay_10", "Purple Hardened Clay")
    STAINED_HARDENED_CLAY_11 = \
        Item(159, "minecraft:stained_hardened_clay_11", "Blue Hardened Clay")
    STAINED_HARDENED_CLAY_12 = \
        Item(159, "minecraft:stained_hardened_clay_12", "Brown Hardened Clay")
    STAINED_HARDENED_CLAY_13 = \
        Item(159, "minecraft:stained_hardened_clay_13", "Green Hardened Clay")
    STAINED_HARDENED_CLAY_14 = \
        Item(159, "minecraft:stained_hardened_clay_14", "Red Hardened Clay")
    STAINED_HARDENED_CLAY_15 = \
        Item(159, "minecraft:stained_hardened_clay_15", "Black Hardened Clay")
    STAINED_GLASS_PANE = \
        Item(160, "minecraft:stained_glass_pane", "White Stained Glass Pane")
    STAINED_GLASS_PANE_1 = \
        Item(160, "minecraft:stained_glass_pane_1", "Orange Stained Glass Pane")
    STAINED_GLASS_PANE_2 = \
        Item(160, "minecraft:stained_glass_pane_2", "Magenta Stained Glass Pane")
    STAINED_GLASS_PANE_3 = \
        Item(160, "minecraft:stained_glass_pane_3", "Light Blue Stained Glass Pane")
    STAINED_GLASS_PANE_4 = \
        Item(160, "minecraft:stained_glass_pane_4", "Yellow Stained Glass Pane")
    STAINED_GLASS_PANE_5 = \
        Item(160, "minecraft:stained_glass_pane_5", "Lime Stained Glass Pane")
    STAINED_GLASS_PANE_6 = \
        Item(160, "minecraft:stained_glass_pane_6", "Pink Stained Glass Pane")
    STAINED_GLASS_PANE_7 = \
        Item(160, "minecraft:stained_glass_pane_7", "Gray Stained Glass Pane")
    STAINED_GLASS_PANE_8 = \
        Item(160, "minecraft:stained_glass_pane_8", "Light Gray Stained Glass Pane")
    STAINED_GLASS_PANE_9 = \
        Item(160, "minecraft:stained_glass_pane_9", "Cyan Stained Glass Pane")
    STAINED_GLASS_PANE_10 = \
        Item(160, "minecraft:stained_glass_pane_10", "Purple Stained Glass Pane")
    STAINED_GLASS_PANE_11 = \
        Item(160, "minecraft:stained_glass_pane_11", "Blue Stained Glass Pane")
    STAINED_GLASS_PANE_12 = \
        Item(160, "minecraft:stained_glass_pane_12", "Brown Stained Glass Pane")
    STAINED_GLASS_PANE_13 = \
        Item(160, "minecraft:stained_glass_pane_13", "Green Stained Glass Pane")
    STAINED_GLASS_PANE_14 = \
        Item(160, "minecraft:stained_glass_pane_14", "Red Stained Glass Pane")
    STAINED_GLASS_PANE_15 = \
        Item(160, "minecraft:stained_glass_pane_15", "Black Stained Glass Pane")
    LEAVES2 = \
        Item(161, "minecraft:leaves2", "Acacia Leaves")
    LEAVES2_1 = \
        Item(161, "minecraft:leaves2_1", "Dark Oak Leaves")
    LOG2 = \
        Item(162, "minecraft:log2", "Acacia Wood")
    LOG2_1 = \
        Item(162, "minecraft:log2_1", "Dark Oak Wood")
    ACACIA_STAIRS = \
        Item(163, "minecraft:acacia_stairs", "Acacia Wood Stairs")
    DARK_OAK_STAIRS = \
        Item(164, "minecraft:dark_oak_stairs", "Dark Oak Wood Stairs")
    SLIME = \
        Item(165, "minecraft:slime", "Slime Block")
    BARRIER = \
        Item(166, "minecraft:barrier", "Barrier")
    IRON_TRAPDOOR = \
        Item(167, "minecraft:iron_trapdoor", "Iron Trapdoor")
    PRISMARINE = \
        Item(168, "minecraft:prismarine", "Prismarine")
    PRISMARINE_1 = \
        Item(168, "minecraft:prismarine_1", "Prismarine Bricks")
    PRISMARINE_2 = \
        Item(168, "minecraft:prismarine_2", "Dark Prismarine")
    SEA_LANTERN = \
        Item(169, "minecraft:sea_lantern", "Sea Lantern")
    HAY_BLOCK = \
        Item(170, "minecraft:hay_block", "Hay Bale")
    CARPET = \
        Item(171, "minecraft:carpet", "White Carpet")
    CARPET_1 = \
        Item(171, "minecraft:carpet_1", "Orange Carpet")
    CARPET_2 = \
        Item(171, "minecraft:carpet_2", "Magenta Carpet")
    CARPET_3 = \
        Item(171, "minecraft:carpet_3", "Light Blue Carpet")
    CARPET_4 = \
        Item(171, "minecraft:carpet_4", "Yellow Carpet")
    CARPET_5 = \
        Item(171, "minecraft:carpet_5", "Lime Carpet")
    CARPET_6 = \
        Item(171, "minecraft:carpet_6", "Pink Carpet")
    CARPET_7 = \
        Item(171, "minecraft:carpet_7", "Gray Carpet")
    CARPET_8 = \
        Item(171, "minecraft:carpet_8", "Light Gray Carpet")
    CARPET_9 = \
        Item(171, "minecraft:carpet_9", "Cyan Carpet")
    CARPET_10 = \
        Item(171, "minecraft:carpet_10", "Purple Carpet")
    CARPET_11 = \
        Item(171, "minecraft:carpet_11", "Blue Carpet")
    CARPET_12 = \
        Item(171, "minecraft:carpet_12", "Brown Carpet")
    CARPET_13 = \
        Item(171, "minecraft:carpet_13", "Green Carpet")
    CARPET_14 = \
        Item(171, "minecraft:carpet_14", "Red Carpet")
    CARPET_15 = \
        Item(171, "minecraft:carpet_15", "Black Carpet")
    HARDENED_CLAY = \
        Item(172, "minecraft:hardened_clay", "Hardened Clay")
    COAL_BLOCK = \
        Item(173, "minecraft:coal_block", "Block of Coal")
    PACKED_ICE = \
        Item(174, "minecraft:packed_ice", "Packed Ice")
    DOUBLE_PLANT = \
        Item(175, "minecraft:double_plant", "Sunflower")
    DOUBLE_PLANT_1 = \
        Item(175, "minecraft:double_plant_1", "Lilac")
    DOUBLE_PLANT_2 = \
        Item(175, "minecraft:double_plant_2", "Double Tallgrass")
    DOUBLE_PLANT_3 = \
        Item(175, "minecraft:double_plant_3", "Large Fern")
    DOUBLE_PLANT_4 = \
        Item(175, "minecraft:double_plant_4", "Rose Bush")
    DOUBLE_PLANT_5 = \
        Item(175, "minecraft:double_plant_5", "Peony")
    STANDING_BANNER = \
        Item(176, "minecraft:standing_banner", "Free-standing Banner")
    WALL_BANNER = \
        Item(177, "minecraft:wall_banner", "Wall-mounted Banner")
    DAYLIGHT_DETECTOR_INVERTED = \
        Item(178, "minecraft:daylight_detector_inverted", "Inverted Daylight Sensor")
    RED_SANDSTONE = \
        Item(179, "minecraft:red_sandstone", "Red Sandstone")
    RED_SANDSTONE_1 = \
        Item(179, "minecraft:red_sandstone_1", "Chiseled Red Sandstone")
    RED_SANDSTONE_2 = \
        Item(179, "minecraft:red_sandstone_2", "Smooth Red Sandstone")
    RED_SANDSTONE_STAIRS = \
        Item(180, "minecraft:red_sandstone_stairs", "Red Sandstone Stairs")
    DOUBLE_STONE_SLAB2 = \
        Item(181, "minecraft:double_stone_slab2", "Double Red Sandstone Slab")
    STONE_SLAB2 = \
        Item(182, "minecraft:stone_slab2", "Red Sandstone Slab")
    SPRUCE_FENCE_GATE = \
        Item(183, "minecraft:spruce_fence_gate", "Spruce Fence Gate")
    BIRCH_FENCE_GATE = \
        Item(184, "minecraft:birch_fence_gate", "Birch Fence Gate")
    JUNGLE_FENCE_GATE = \
        Item(185, "minecraft:jungle_fence_gate", "Jungle Fence Gate")
    DARK_OAK_FENCE_GATE = \
        Item(186, "minecraft:dark_oak_fence_gate", "Dark Oak Fence Gate")
    ACACIA_FENCE_GATE = \
        Item(187, "minecraft:acacia_fence_gate", "Acacia Fence Gate")
    SPRUCE_FENCE = \
        Item(188, "minecraft:spruce_fence", "Spruce Fence")
    BIRCH_FENCE = \
        Item(189, "minecraft:birch_fence", "Birch Fence")
    JUNGLE_FENCE = \
        Item(190, "minecraft:jungle_fence", "Jungle Fence")
    DARK_OAK_FENCE = \
        Item(191, "minecraft:dark_oak_fence", "Dark Oak Fence")
    ACACIA_FENCE = \
        Item(192, "minecraft:acacia_fence", "Acacia Fence")
    SPRUCE_DOOR = \
        Item(193, "minecraft:spruce_door", "Spruce Door Block")
    BIRCH_DOOR = \
        Item(194, "minecraft:birch_door", "Birch Door Block")
    JUNGLE_DOOR = \
        Item(195, "minecraft:jungle_door", "Jungle Door Block")
    ACACIA_DOOR = \
        Item(196, "minecraft:acacia_door", "Acacia Door Block")
    DARK_OAK_DOOR = \
        Item(197, "minecraft:dark_oak_door", "Dark Oak Door Block")
    END_ROD = \
        Item(198, "minecraft:end_rod", "End Rod")
    CHORUS_PLANT = \
        Item(199, "minecraft:chorus_plant", "Chorus Plant")
    CHORUS_FLOWER = \
        Item(200, "minecraft:chorus_flower", "Chorus Flower")
    PURPUR_BLOCK = \
        Item(201, "minecraft:purpur_block", "Purpur Block")
    PURPUR_PILLAR = \
        Item(202, "minecraft:purpur_pillar", "Purpur Pillar")
    PURPUR_STAIRS = \
        Item(203, "minecraft:purpur_stairs", "Purpur Stairs")
    PURPUR_DOUBLE_SLAB = \
        Item(204, "minecraft:purpur_double_slab", "Purpur Double Slab")
    PURPUR_SLAB = \
        Item(205, "minecraft:purpur_slab", "Purpur Slab")
    END_BRICKS = \
        Item(206, "minecraft:end_bricks", "End Stone Bricks")
    BEETROOTS = \
        Item(207, "minecraft:beetroots", "Beetroot Block")
    GRASS_PATH = \
        Item(208, "minecraft:grass_path", "Grass Path")
    END_GATEWAY = \
        Item(209, "minecraft:end_gateway", "End Gateway")
    REPEATING_COMMAND_BLOCK = \
        Item(210, "minecraft:repeating_command_block", "Repeating Command Block")
    CHAIN_COMMAND_BLOCK = \
        Item(211, "minecraft:chain_command_block", "Chain Command Block")
    FROSTED_ICE = \
        Item(212, "minecraft:frosted_ice", "Frosted Ice")
    MAGMA = \
        Item(213, "minecraft:magma", "Magma Block")
    NETHER_WART_BLOCK = \
        Item(214, "minecraft:nether_wart_block", "Nether Wart Block")
    RED_NETHER_BRICK = \
        Item(215, "minecraft:red_nether_brick", "Red Nether Brick")
    BONE_BLOCK = \
        Item(216, "minecraft:bone_block", "Bone Block")
    STRUCTURE_VOID = \
        Item(217, "minecraft:structure_void", "Structure Void")
    OBSERVER = \
        Item(218, "minecraft:observer", "Observer")
    WHITE_SHULKER_BOX = \
        Item(219, "minecraft:white_shulker_box", "White Shulker Box")
    ORANGE_SHULKER_BOX = \
        Item(220, "minecraft:orange_shulker_box", "Orange Shulker Box")
    MAGENTA_SHULKER_BOX = \
        Item(221, "minecraft:magenta_shulker_box", "Magenta Shulker Box")
    LIGHT_BLUE_SHULKER_BOX = \
        Item(222, "minecraft:light_blue_shulker_box", "Light Blue Shulker Box")
    YELLOW_SHULKER_BOX = \
        Item(223, "minecraft:yellow_shulker_box", "Yellow Shulker Box")
    LIME_SHULKER_BOX = \
        Item(224, "minecraft:lime_shulker_box", "Lime Shulker Box")
    PINK_SHULKER_BOX = \
        Item(225, "minecraft:pink_shulker_box", "Pink Shulker Box")
    GRAY_SHULKER_BOX = \
        Item(226, "minecraft:gray_shulker_box", "Gray Shulker Box")
    SILVER_SHULKER_BOX = \
        Item(227, "minecraft:silver_shulker_box", "Light Gray Shulker Box")
    CYAN_SHULKER_BOX = \
        Item(228, "minecraft:cyan_shulker_box", "Cyan Shulker Box")
    PURPLE_SHULKER_BOX = \
        Item(229, "minecraft:purple_shulker_box", "Purple Shulker Box")
    BLUE_SHULKER_BOX = \
        Item(230, "minecraft:blue_shulker_box", "Blue Shulker Box")
    BROWN_SHULKER_BOX = \
        Item(231, "minecraft:brown_shulker_box", "Brown Shulker Box")
    GREEN_SHULKER_BOX = \
        Item(232, "minecraft:green_shulker_box", "Green Shulker Box")
    RED_SHULKER_BOX = \
        Item(233, "minecraft:red_shulker_box", "Red Shulker Box")
    BLACK_SHULKER_BOX = \
        Item(234, "minecraft:black_shulker_box", "Black Shulker Box")
    WHITE_GLAZED_TERRACOTTA = \
        Item(235, "minecraft:white_glazed_terracotta", "White Glazed Terracotta")
    ORANGE_GLAZED_TERRACOTTA = \
        Item(236, "minecraft:orange_glazed_terracotta", "Orange Glazed Terracotta")
    MAGENTA_GLAZED_TERRACOTTA = \
        Item(237, "minecraft:magenta_glazed_terracotta", "Magenta Glazed Terracotta")
    LIGHT_BLUE_GLAZED_TERRACOTTA = \
        Item(238, "minecraft:light_blue_glazed_terracotta", "Light Blue Glazed Terracotta")
    YELLOW_GLAZED_TERRACOTTA = \
        Item(239, "minecraft:yellow_glazed_terracotta", "Yellow Glazed Terracotta")
    LIME_GLAZED_TERRACOTTA = \
        Item(240, "minecraft:lime_glazed_terracotta", "Lime Glazed Terracotta")
    PINK_GLAZED_TERRACOTTA = \
        Item(241, "minecraft:pink_glazed_terracotta", "Pink Glazed Terracotta")
    GRAY_GLAZED_TERRACOTTA = \
        Item(242, "minecraft:gray_glazed_terracotta", "Gray Glazed Terracotta")
    LIGHT_GRAY_GLAZED_TERRACOTTA = \
        Item(243, "minecraft:light_gray_glazed_terracotta", "Light Gray Glazed Terracotta")
    CYAN_GLAZED_TERRACOTTA = \
        Item(244, "minecraft:cyan_glazed_terracotta", "Cyan Glazed Terracotta")
    PURPLE_GLAZED_TERRACOTTA = \
        Item(245, "minecraft:purple_glazed_terracotta", "Purple Glazed Terracotta")
    BLUE_GLAZED_TERRACOTTA = \
        Item(246, "minecraft:blue_glazed_terracotta", "Blue Glazed Terracotta")
    BROWN_GLAZED_TERRACOTTA = \
        Item(247, "minecraft:brown_glazed_terracotta", "Brown Glazed Terracotta")
    GREEN_GLAZED_TERRACOTTA = \
        Item(248, "minecraft:green_glazed_terracotta", "Green Glazed Terracotta")
    RED_GLAZED_TERRACOTTA = \
        Item(249, "minecraft:red_glazed_terracotta", "Red Glazed Terracotta")
    BLACK_GLAZED_TERRACOTTA = \
        Item(250, "minecraft:black_glazed_terracotta", "Black Glazed Terracotta")
    CONCRETE = \
        Item(251, "minecraft:concrete", "White Concrete")
    CONCRETE_1 = \
        Item(251, "minecraft:concrete_1", "Orange Concrete")
    CONCRETE_2 = \
        Item(251, "minecraft:concrete_2", "Magenta Concrete")
    CONCRETE_3 = \
        Item(251, "minecraft:concrete_3", "Light Blue Concrete")
    CONCRETE_4 = \
        Item(251, "minecraft:concrete_4", "Yellow Concrete")
    CONCRETE_5 = \
        Item(251, "minecraft:concrete_5", "Lime Concrete")
    CONCRETE_6 = \
        Item(251, "minecraft:concrete_6", "Pink Concrete")
    CONCRETE_7 = \
        Item(251, "minecraft:concrete_7", "Gray Concrete")
    CONCRETE_8 = \
        Item(251, "minecraft:concrete_8", "Light Gray Concrete")
    CONCRETE_9 = \
        Item(251, "minecraft:concrete_9", "Cyan Concrete")
    CONCRETE_10 = \
        Item(251, "minecraft:concrete_10", "Purple Concrete")
    CONCRETE_11 = \
        Item(251, "minecraft:concrete_11", "Blue Concrete")
    CONCRETE_12 = \
        Item(251, "minecraft:concrete_12", "Brown Concrete")
    CONCRETE_13 = \
        Item(251, "minecraft:concrete_13", "Green Concrete")
    CONCRETE_14 = \
        Item(251, "minecraft:concrete_14", "Red Concrete")
    CONCRETE_15 = \
        Item(251, "minecraft:concrete_15", "Black Concrete")
    CONCRETE_POWDER = \
        Item(252, "minecraft:concrete_powder", "White Concrete Powder")
    CONCRETE_POWDER_1 = \
        Item(252, "minecraft:concrete_powder_1", "Orange Concrete Powder")
    CONCRETE_POWDER_2 = \
        Item(252, "minecraft:concrete_powder_2", "Magenta Concrete Powder")
    CONCRETE_POWDER_3 = \
        Item(252, "minecraft:concrete_powder_3", "Light Blue Concrete Powder")
    CONCRETE_POWDER_4 = \
        Item(252, "minecraft:concrete_powder_4", "Yellow Concrete Powder")
    CONCRETE_POWDER_5 = \
        Item(252, "minecraft:concrete_powder_5", "Lime Concrete Powder")
    CONCRETE_POWDER_6 = \
        Item(252, "minecraft:concrete_powder_6", "Pink Concrete Powder")
    CONCRETE_POWDER_7 = \
        Item(252, "minecraft:concrete_powder_7", "Gray Concrete Powder")
    CONCRETE_POWDER_8 = \
        Item(252, "minecraft:concrete_powder_8", "Light Gray Concrete Powder")
    CONCRETE_POWDER_9 = \
        Item(252, "minecraft:concrete_powder_9", "Cyan Concrete Powder")
    CONCRETE_POWDER_10 = \
        Item(252, "minecraft:concrete_powder_10", "Purple Concrete Powder")
    CONCRETE_POWDER_11 = \
        Item(252, "minecraft:concrete_powder_11", "Blue Concrete Powder")
    CONCRETE_POWDER_12 = \
        Item(252, "minecraft:concrete_powder_12", "Brown Concrete Powder")
    CONCRETE_POWDER_13 = \
        Item(252, "minecraft:concrete_powder_13", "Green Concrete Powder")
    CONCRETE_POWDER_14 = \
        Item(252, "minecraft:concrete_powder_14", "Red Concrete Powder")
    CONCRETE_POWDER_15 = \
        Item(252, "minecraft:concrete_powder_15", "Black Concrete Powder")
    STRUCTURE_BLOCK = \
        Item(255, "minecraft:structure_block", "Structure Block")
    IRON_SHOVEL = \
        Item(256, "minecraft:iron_shovel", "Iron Shovel")
    IRON_PICKAXE = \
        Item(257, "minecraft:iron_pickaxe", "Iron Pickaxe")
    IRON_AXE = \
        Item(258, "minecraft:iron_axe", "Iron Axe")
    FLINT_AND_STEEL = \
        Item(259, "minecraft:flint_and_steel", "Flint and Steel")
    APPLE = \
        Item(260, "minecraft:apple", "Apple")
    BOW = \
        Item(261, "minecraft:bow", "Bow")
    ARROW = \
        Item(262, "minecraft:arrow", "Arrow")
    COAL = \
        Item(263, "minecraft:coal", "Coal")
    COAL_1 = \
        Item(263, "minecraft:coal_1", "Charcoal")
    DIAMOND = \
        Item(264, "minecraft:diamond", "Diamond")
    IRON_INGOT = \
        Item(265, "minecraft:iron_ingot", "Iron Ingot")
    GOLD_INGOT = \
        Item(266, "minecraft:gold_ingot", "Gold Ingot")
    IRON_SWORD = \
        Item(267, "minecraft:iron_sword", "Iron Sword")
    WOODEN_SWORD = \
        Item(268, "minecraft:wooden_sword", "Wooden Sword")
    WOODEN_SHOVEL = \
        Item(269, "minecraft:wooden_shovel", "Wooden Shovel")
    WOODEN_PICKAXE = \
        Item(270, "minecraft:wooden_pickaxe", "Wooden Pickaxe")
    WOODEN_AXE = \
        Item(271, "minecraft:wooden_axe", "Wooden Axe")
    STONE_SWORD = \
        Item(272, "minecraft:stone_sword", "Stone Sword")
    STONE_SHOVEL = \
        Item(273, "minecraft:stone_shovel", "Stone Shovel")
    STONE_PICKAXE = \
        Item(274, "minecraft:stone_pickaxe", "Stone Pickaxe")
    STONE_AXE = \
        Item(275, "minecraft:stone_axe", "Stone Axe")
    DIAMOND_SWORD = \
        Item(276, "minecraft:diamond_sword", "Diamond Sword")
    DIAMOND_SHOVEL = \
        Item(277, "minecraft:diamond_shovel", "Diamond Shovel")
    DIAMOND_PICKAXE = \
        Item(278, "minecraft:diamond_pickaxe", "Diamond Pickaxe")
    DIAMOND_AXE = \
        Item(279, "minecraft:diamond_axe", "Diamond Axe")
    STICK = \
        Item(280, "minecraft:stick", "Stick")
    BOWL = \
        Item(281, "minecraft:bowl", "Bowl")
    MUSHROOM_STEW = \
        Item(282, "minecraft:mushroom_stew", "Mushroom Stew")
    GOLDEN_SWORD = \
        Item(283, "minecraft:golden_sword", "Golden Sword")
    GOLDEN_SHOVEL = \
        Item(284, "minecraft:golden_shovel", "Golden Shovel")
    GOLDEN_PICKAXE = \
        Item(285, "minecraft:golden_pickaxe", "Golden Pickaxe")
    GOLDEN_AXE = \
        Item(286, "minecraft:golden_axe", "Golden Axe")
    STRING = \
        Item(287, "minecraft:string", "String")
    FEATHER = \
        Item(288, "minecraft:feather", "Feather")
    GUNPOWDER = \
        Item(289, "minecraft:gunpowder", "Gunpowder")
    WOODEN_HOE = \
        Item(290, "minecraft:wooden_hoe", "Wooden Hoe")
    STONE_HOE = \
        Item(291, "minecraft:stone_hoe", "Stone Hoe")
    IRON_HOE = \
        Item(292, "minecraft:iron_hoe", "Iron Hoe")
    DIAMOND_HOE = \
        Item(293, "minecraft:diamond_hoe", "Diamond Hoe")
    GOLDEN_HOE = \
        Item(294, "minecraft:golden_hoe", "Golden Hoe")
    WHEAT_SEEDS = \
        Item(295, "minecraft:wheat_seeds", "Wheat Seeds")
    WHEAT = \
        Item(296, "minecraft:wheat", "Wheat")
    BREAD = \
        Item(297, "minecraft:bread", "Bread")
    LEATHER_HELMET = \
        Item(298, "minecraft:leather_helmet", "Leather Helmet")
    LEATHER_CHESTPLATE = \
        Item(299, "minecraft:leather_chestplate", "Leather Tunic")
    LEATHER_LEGGINGS = \
        Item(300, "minecraft:leather_leggings", "Leather Pants")
    LEATHER_BOOTS = \
        Item(301, "minecraft:leather_boots", "Leather Boots")
    CHAINMAIL_HELMET = \
        Item(302, "minecraft:chainmail_helmet", "Chainmail Helmet")
    CHAINMAIL_CHESTPLATE = \
        Item(303, "minecraft:chainmail_chestplate", "Chainmail Chestplate")
    CHAINMAIL_LEGGINGS = \
        Item(304, "minecraft:chainmail_leggings", "Chainmail Leggings")
    CHAINMAIL_BOOTS = \
        Item(305, "minecraft:chainmail_boots", "Chainmail Boots")
    IRON_HELMET = \
        Item(306, "minecraft:iron_helmet", "Iron Helmet")
    IRON_CHESTPLATE = \
        Item(307, "minecraft:iron_chestplate", "Iron Chestplate")
    IRON_LEGGINGS = \
        Item(308, "minecraft:iron_leggings", "Iron Leggings")
    IRON_BOOTS = \
        Item(309, "minecraft:iron_boots", "Iron Boots")
    DIAMOND_HELMET = \
        Item(310, "minecraft:diamond_helmet", "Diamond Helmet")
    DIAMOND_CHESTPLATE = \
        Item(311, "minecraft:diamond_chestplate", "Diamond Chestplate")
    DIAMOND_LEGGINGS = \
        Item(312, "minecraft:diamond_leggings", "Diamond Leggings")
    DIAMOND_BOOTS = \
        Item(313, "minecraft:diamond_boots", "Diamond Boots")
    GOLDEN_HELMET = \
        Item(314, "minecraft:golden_helmet", "Golden Helmet")
    GOLDEN_CHESTPLATE = \
        Item(315, "minecraft:golden_chestplate", "Golden Chestplate")
    GOLDEN_LEGGINGS = \
        Item(316, "minecraft:golden_leggings", "Golden Leggings")
    GOLDEN_BOOTS = \
        Item(317, "minecraft:golden_boots", "Golden Boots")
    FLINT = \
        Item(318, "minecraft:flint", "Flint")
    PORKCHOP = \
        Item(319, "minecraft:porkchop", "Raw Porkchop")
    COOKED_PORKCHOP = \
        Item(320, "minecraft:cooked_porkchop", "Cooked Porkchop")
    PAINTING = \
        Item(321, "minecraft:painting", "Painting")
    GOLDEN_APPLE = \
        Item(322, "minecraft:golden_apple", "Golden Apple")
    GOLDEN_APPLE_1 = \
        Item(322, "minecraft:golden_apple_1", "Enchanted Golden Apple")
    SIGN = \
        Item(323, "minecraft:sign", "Sign")
    WOODEN_DOOR = \
        Item(324, "minecraft:wooden_door", "Oak Door")
    BUCKET = \
        Item(325, "minecraft:bucket", "Bucket")
    WATER_BUCKET = \
        Item(326, "minecraft:water_bucket", "Water Bucket")
    LAVA_BUCKET = \
        Item(327, "minecraft:lava_bucket", "Lava Bucket")
    MINECART = \
        Item(328, "minecraft:minecart", "Minecart")
    SADDLE = \
        Item(329, "minecraft:saddle", "Saddle")
    IRON_DOOR = \
        Item(330, "minecraft:iron_door", "Iron Door")
    REDSTONE = \
        Item(331, "minecraft:redstone", "Redstone")
    SNOWBALL = \
        Item(332, "minecraft:snowball", "Snowball")
    BOAT = \
        Item(333, "minecraft:boat", "Oak Boat")
    LEATHER = \
        Item(334, "minecraft:leather", "Leather")
    MILK_BUCKET = \
        Item(335, "minecraft:milk_bucket", "Milk Bucket")
    BRICK = \
        Item(336, "minecraft:brick", "Brick")
    CLAY_BALL = \
        Item(337, "minecraft:clay_ball", "Clay")
    REEDS = \
        Item(338, "minecraft:reeds", "Sugar Canes")
    PAPER = \
        Item(339, "minecraft:paper", "Paper")
    BOOK = \
        Item(340, "minecraft:book", "Book")
    SLIME_BALL = \
        Item(341, "minecraft:slime_ball", "Slimeball")
    CHEST_MINECART = \
        Item(342, "minecraft:chest_minecart", "Minecart with Chest")
    FURNACE_MINECART = \
        Item(343, "minecraft:furnace_minecart", "Minecart with Furnace")
    EGG = \
        Item(344, "minecraft:egg", "Egg")
    COMPASS = \
        Item(345, "minecraft:compass", "Compass")
    FISHING_ROD = \
        Item(346, "minecraft:fishing_rod", "Fishing Rod")
    CLOCK = \
        Item(347, "minecraft:clock", "Clock")
    GLOWSTONE_DUST = \
        Item(348, "minecraft:glowstone_dust", "Glowstone Dust")
    FISH = \
        Item(349, "minecraft:fish", "Raw Fish")
    FISH_1 = \
        Item(349, "minecraft:fish_1", "Raw Salmon")
    FISH_2 = \
        Item(349, "minecraft:fish_2", "Clownfish")
    FISH_3 = \
        Item(349, "minecraft:fish_3", "Pufferfish")
    COOKED_FISH = \
        Item(350, "minecraft:cooked_fish", "Cooked Fish")
    COOKED_FISH_1 = \
        Item(350, "minecraft:cooked_fish_1", "Cooked Salmon")
    DYE = \
        Item(351, "minecraft:dye", "Ink Sack")
    DYE_1 = \
        Item(351, "minecraft:dye_1", "Rose Red")
    DYE_2 = \
        Item(351, "minecraft:dye_2", "Cactus Green")
    DYE_3 = \
        Item(351, "minecraft:dye_3", "Coco Beans")
    DYE_4 = \
        Item(351, "minecraft:dye_4", "Lapis Lazuli")
    DYE_5 = \
        Item(351, "minecraft:dye_5", "Purple Dye")
    DYE_6 = \
        Item(351, "minecraft:dye_6", "Cyan Dye")
    DYE_7 = \
        Item(351, "minecraft:dye_7", "Light Gray Dye")
    DYE_8 = \
        Item(351, "minecraft:dye_8", "Gray Dye")
    DYE_9 = \
        Item(351, "minecraft:dye_9", "Pink Dye")
    DYE_10 = \
        Item(351, "minecraft:dye_10", "Lime Dye")
    DYE_11 = \
        Item(351, "minecraft:dye_11", "Dandelion Yellow")
    DYE_12 = \
        Item(351, "minecraft:dye_12", "Light Blue Dye")
    DYE_13 = \
        Item(351, "minecraft:dye_13", "Magenta Dye")
    DYE_14 = \
        Item(351, "minecraft:dye_14", "Orange Dye")
    DYE_15 = \
        Item(351, "minecraft:dye_15", "Bone Meal")
    BONE = \
        Item(352, "minecraft:bone", "Bone")
    SUGAR = \
        Item(353, "minecraft:sugar", "Sugar")
    CAKE = \
        Item(354, "minecraft:cake", "Cake")
    BED = \
        Item(355, "minecraft:bed", "Bed")
    REPEATER = \
        Item(356, "minecraft:repeater", "Redstone Repeater")
    COOKIE = \
        Item(357, "minecraft:cookie", "Cookie")
    FILLED_MAP = \
        Item(358, "minecraft:filled_map", "Map")
    SHEARS = \
        Item(359, "minecraft:shears", "Shears")
    MELON = \
        Item(360, "minecraft:melon", "Melon")
    PUMPKIN_SEEDS = \
        Item(361, "minecraft:pumpkin_seeds", "Pumpkin Seeds")
    MELON_SEEDS = \
        Item(362, "minecraft:melon_seeds", "Melon Seeds")
    BEEF = \
        Item(363, "minecraft:beef", "Raw Beef")
    COOKED_BEEF = \
        Item(364, "minecraft:cooked_beef", "Steak")
    CHICKEN = \
        Item(365, "minecraft:chicken", "Raw Chicken")
    COOKED_CHICKEN = \
        Item(366, "minecraft:cooked_chicken", "Cooked Chicken")
    ROTTEN_FLESH = \
        Item(367, "minecraft:rotten_flesh", "Rotten Flesh")
    ENDER_PEARL = \
        Item(368, "minecraft:ender_pearl", "Ender Pearl")
    BLAZE_ROD = \
        Item(369, "minecraft:blaze_rod", "Blaze Rod")
    GHAST_TEAR = \
        Item(370, "minecraft:ghast_tear", "Ghast Tear")
    GOLD_NUGGET = \
        Item(371, "minecraft:gold_nugget", "Gold Nugget")
    NETHER_WART = \
        Item(372, "minecraft:nether_wart", "Nether Wart")
    POTION = \
        Item(373, "minecraft:potion", "Potion")
    GLASS_BOTTLE = \
        Item(374, "minecraft:glass_bottle", "Glass Bottle")
    SPIDER_EYE = \
        Item(375, "minecraft:spider_eye", "Spider Eye")
    FERMENTED_SPIDER_EYE = \
        Item(376, "minecraft:fermented_spider_eye", "Fermented Spider Eye")
    BLAZE_POWDER = \
        Item(377, "minecraft:blaze_powder", "Blaze Powder")
    MAGMA_CREAM = \
        Item(378, "minecraft:magma_cream", "Magma Cream")
    BREWING_STAND = \
        Item(379, "minecraft:brewing_stand", "Brewing Stand")
    CAULDRON = \
        Item(380, "minecraft:cauldron", "Cauldron")
    ENDER_EYE = \
        Item(381, "minecraft:ender_eye", "Eye of Ender")
    SPECKLED_MELON = \
        Item(382, "minecraft:speckled_melon", "Glistering Melon")
    SPAWN_EGG_4 = \
        Item(383, "minecraft:spawn_egg_4", "Spawn Elder Guardian")
    SPAWN_EGG_5 = \
        Item(383, "minecraft:spawn_egg_5", "Spawn Wither Skeleton")
    SPAWN_EGG_6 = \
        Item(383, "minecraft:spawn_egg_6", "Spawn Stray")
    SPAWN_EGG_23 = \
        Item(383, "minecraft:spawn_egg_23", "Spawn Husk")
    SPAWN_EGG_27 = \
        Item(383, "minecraft:spawn_egg_27", "Spawn Zombie Villager")
    SPAWN_EGG_28 = \
        Item(383, "minecraft:spawn_egg_28", "Spawn Skeleton Horse")
    SPAWN_EGG_29 = \
        Item(383, "minecraft:spawn_egg_29", "Spawn Zombie Horse")
    SPAWN_EGG_31 = \
        Item(383, "minecraft:spawn_egg_31", "Spawn Donkey")
    SPAWN_EGG_32 = \
        Item(383, "minecraft:spawn_egg_32", "Spawn Mule")
    SPAWN_EGG_34 = \
        Item(383, "minecraft:spawn_egg_34", "Spawn Evoker")
    SPAWN_EGG_35 = \
        Item(383, "minecraft:spawn_egg_35", "Spawn Vex")
    SPAWN_EGG_36 = \
        Item(383, "minecraft:spawn_egg_36", "Spawn Vindicator")
    SPAWN_EGG_50 = \
        Item(383, "minecraft:spawn_egg_50", "Spawn Creeper")
    SPAWN_EGG_51 = \
        Item(383, "minecraft:spawn_egg_51", "Spawn Skeleton")
    SPAWN_EGG_52 = \
        Item(383, "minecraft:spawn_egg_52", "Spawn Spider")
    SPAWN_EGG_54 = \
        Item(383, "minecraft:spawn_egg_54", "Spawn Zombie")
    SPAWN_EGG_55 = \
        Item(383, "minecraft:spawn_egg_55", "Spawn Slime")
    SPAWN_EGG_56 = \
        Item(383, "minecraft:spawn_egg_56", "Spawn Ghast")
    SPAWN_EGG_57 = \
        Item(383, "minecraft:spawn_egg_57", "Spawn Zombie Pigman")
    SPAWN_EGG_58 = \
        Item(383, "minecraft:spawn_egg_58", "Spawn Enderman")
    SPAWN_EGG_59 = \
        Item(383, "minecraft:spawn_egg_59", "Spawn Cave Spider")
    SPAWN_EGG_60 = \
        Item(383, "minecraft:spawn_egg_60", "Spawn Silverfish")
    SPAWN_EGG_61 = \
        Item(383, "minecraft:spawn_egg_61", "Spawn Blaze")
    SPAWN_EGG_62 = \
        Item(383, "minecraft:spawn_egg_62", "Spawn Magma Cube")
    SPAWN_EGG_65 = \
        Item(383, "minecraft:spawn_egg_65", "Spawn Bat")
    SPAWN_EGG_66 = \
        Item(383, "minecraft:spawn_egg_66", "Spawn Witch")
    SPAWN_EGG_67 = \
        Item(383, "minecraft:spawn_egg_67", "Spawn Endermite")
    SPAWN_EGG_68 = \
        Item(383, "minecraft:spawn_egg_68", "Spawn Guardian")
    SPAWN_EGG_69 = \
        Item(383, "minecraft:spawn_egg_69", "Spawn Shulker")
    SPAWN_EGG_90 = \
        Item(383, "minecraft:spawn_egg_90", "Spawn Pig")
    SPAWN_EGG_91 = \
        Item(383, "minecraft:spawn_egg_91", "Spawn Sheep")
    SPAWN_EGG_92 = \
        Item(383, "minecraft:spawn_egg_92", "Spawn Cow")
    SPAWN_EGG_93 = \
        Item(383, "minecraft:spawn_egg_93", "Spawn Chicken")
    SPAWN_EGG_94 = \
        Item(383, "minecraft:spawn_egg_94", "Spawn Squid")
    SPAWN_EGG_95 = \
        Item(383, "minecraft:spawn_egg_95", "Spawn Wolf")
    SPAWN_EGG_96 = \
        Item(383, "minecraft:spawn_egg_96", "Spawn Mooshroom")
    SPAWN_EGG_98 = \
        Item(383, "minecraft:spawn_egg_98", "Spawn Ocelot")
    SPAWN_EGG_100 = \
        Item(383, "minecraft:spawn_egg_100", "Spawn Horse")
    SPAWN_EGG_101 = \
        Item(383, "minecraft:spawn_egg_101", "Spawn Rabbit")
    SPAWN_EGG_102 = \
        Item(383, "minecraft:spawn_egg_102", "Spawn Polar Bear")
    SPAWN_EGG_103 = \
        Item(383, "minecraft:spawn_egg_103", "Spawn Llama")
    SPAWN_EGG_105 = \
        Item(383, "minecraft:spawn_egg_105", "Spawn Parrot")
    SPAWN_EGG_120 = \
        Item(383, "minecraft:spawn_egg_120", "Spawn Villager")
    EXPERIENCE_BOTTLE = \
        Item(384, "minecraft:experience_bottle", "Bottle o' Enchanting")
    FIRE_CHARGE = \
        Item(385, "minecraft:fire_charge", "Fire Charge")
    WRITABLE_BOOK = \
        Item(386, "minecraft:writable_book", "Book and Quill")
    WRITTEN_BOOK = \
        Item(387, "minecraft:written_book", "Written Book")
    EMERALD = \
        Item(388, "minecraft:emerald", "Emerald")
    ITEM_FRAME = \
        Item(389, "minecraft:item_frame", "Item Frame")
    FLOWER_POT = \
        Item(390, "minecraft:flower_pot", "Flower Pot")
    CARROT = \
        Item(391, "minecraft:carrot", "Carrot")
    POTATO = \
        Item(392, "minecraft:potato", "Potato")
    BAKED_POTATO = \
        Item(393, "minecraft:baked_potato", "Baked Potato")
    POISONOUS_POTATO = \
        Item(394, "minecraft:poisonous_potato", "Poisonous Potato")
    MAP = \
        Item(395, "minecraft:map", "Empty Map")
    GOLDEN_CARROT = \
        Item(396, "minecraft:golden_carrot", "Golden Carrot")
    SKULL = \
        Item(397, "minecraft:skull", "Mob Head (Skeleton)")
    SKULL_1 = \
        Item(397, "minecraft:skull_1", "Mob Head (Wither Skeleton)")
    SKULL_2 = \
        Item(397, "minecraft:skull_2", "Mob Head (Zombie)")
    SKULL_3 = \
        Item(397, "minecraft:skull_3", "Mob Head (Human)")
    SKULL_4 = \
        Item(397, "minecraft:skull_4", "Mob Head (Creeper)")
    SKULL_5 = \
        Item(397, "minecraft:skull_5", "Mob Head (Dragon)")
    CARROT_ON_A_STICK = \
        Item(398, "minecraft:carrot_on_a_stick", "Carrot on a Stick")
    NETHER_STAR = \
        Item(399, "minecraft:nether_star", "Nether Star")
    PUMPKIN_PIE = \
        Item(400, "minecraft:pumpkin_pie", "Pumpkin Pie")
    FIREWORKS = \
        Item(401, "minecraft:fireworks", "Firework Rocket")
    FIREWORK_CHARGE = \
        Item(402, "minecraft:firework_charge", "Firework Star")
    ENCHANTED_BOOK = \
        Item(403, "minecraft:enchanted_book", "Enchanted Book")
    COMPARATOR = \
        Item(404, "minecraft:comparator", "Redstone Comparator")
    NETHERBRICK = \
        Item(405, "minecraft:netherbrick", "Nether Brick")
    QUARTZ = \
        Item(406, "minecraft:quartz", "Nether Quartz")
    TNT_MINECART = \
        Item(407, "minecraft:tnt_minecart", "Minecart with TNT")
    HOPPER_MINECART = \
        Item(408, "minecraft:hopper_minecart", "Minecart with Hopper")
    PRISMARINE_SHARD = \
        Item(409, "minecraft:prismarine_shard", "Prismarine Shard")
    PRISMARINE_CRYSTALS = \
        Item(410, "minecraft:prismarine_crystals", "Prismarine Crystals")
    RABBIT = \
        Item(411, "minecraft:rabbit", "Raw Rabbit")
    COOKED_RABBIT = \
        Item(412, "minecraft:cooked_rabbit", "Cooked Rabbit")
    RABBIT_STEW = \
        Item(413, "minecraft:rabbit_stew", "Rabbit Stew")
    RABBIT_FOOT = \
        Item(414, "minecraft:rabbit_foot", "Rabbit's Foot")
    RABBIT_HIDE = \
        Item(415, "minecraft:rabbit_hide", "Rabbit Hide")
    ARMOR_STAND = \
        Item(416, "minecraft:armor_stand", "Armor Stand")
    IRON_HORSE_ARMOR = \
        Item(417, "minecraft:iron_horse_armor", "Iron Horse Armor")
    GOLDEN_HORSE_ARMOR = \
        Item(418, "minecraft:golden_horse_armor", "Golden Horse Armor")
    DIAMOND_HORSE_ARMOR = \
        Item(419, "minecraft:diamond_horse_armor", "Diamond Horse Armor")
    LEAD = \
        Item(420, "minecraft:lead", "Lead")
    NAME_TAG = \
        Item(421, "minecraft:name_tag", "Name Tag")
    COMMAND_BLOCK_MINECART = \
        Item(422, "minecraft:command_block_minecart", "Minecart with Command Block")
    MUTTON = \
        Item(423, "minecraft:mutton", "Raw Mutton")
    COOKED_MUTTON = \
        Item(424, "minecraft:cooked_mutton", "Cooked Mutton")
    BANNER = \
        Item(425, "minecraft:banner", "Banner")
    END_CRYSTAL = \
        Item(426, "minecraft:end_crystal", "End Crystal")
    SPRUCE_DOOR = \
        Item(427, "minecraft:spruce_door", "Spruce Door")
    BIRCH_DOOR = \
        Item(428, "minecraft:birch_door", "Birch Door")
    JUNGLE_DOOR = \
        Item(429, "minecraft:jungle_door", "Jungle Door")
    ACACIA_DOOR = \
        Item(430, "minecraft:acacia_door", "Acacia Door")
    DARK_OAK_DOOR = \
        Item(431, "minecraft:dark_oak_door", "Dark Oak Door")
    CHORUS_FRUIT = \
        Item(432, "minecraft:chorus_fruit", "Chorus Fruit")
    POPPED_CHORUS_FRUIT = \
        Item(433, "minecraft:popped_chorus_fruit", "Popped Chorus Fruit")
    BEETROOT = \
        Item(434, "minecraft:beetroot", "Beetroot")
    BEETROOT_SEEDS = \
        Item(435, "minecraft:beetroot_seeds", "Beetroot Seeds")
    BEETROOT_SOUP = \
        Item(436, "minecraft:beetroot_soup", "Beetroot Soup")
    DRAGON_BREATH = \
        Item(437, "minecraft:dragon_breath", "Dragon's Breath")
    SPLASH_POTION = \
        Item(438, "minecraft:splash_potion", "Splash Potion")
    SPECTRAL_ARROW = \
        Item(439, "minecraft:spectral_arrow", "Spectral Arrow")
    TIPPED_ARROW = \
        Item(440, "minecraft:tipped_arrow", "Tipped Arrow")
    LINGERING_POTION = \
        Item(441, "minecraft:lingering_potion", "Lingering Potion")
    SHIELD = \
        Item(442, "minecraft:shield", "Shield")
    ELYTRA = \
        Item(443, "minecraft:elytra", "Elytra")
    SPRUCE_BOAT = \
        Item(444, "minecraft:spruce_boat", "Spruce Boat")
    BIRCH_BOAT = \
        Item(445, "minecraft:birch_boat", "Birch Boat")
    JUNGLE_BOAT = \
        Item(446, "minecraft:jungle_boat", "Jungle Boat")
    ACACIA_BOAT = \
        Item(447, "minecraft:acacia_boat", "Acacia Boat")
    DARK_OAK_BOAT = \
        Item(448, "minecraft:dark_oak_boat", "Dark Oak Boat")
    TOTEM_OF_UNDYING = \
        Item(449, "minecraft:totem_of_undying", "Totem of Undying")
    SHULKER_SHELL = \
        Item(450, "minecraft:shulker_shell", "Shulker Shell")
    IRON_NUGGET = \
        Item(452, "minecraft:iron_nugget", "Iron Nugget")
    KNOWLEDGE_BOOK = \
        Item(453, "minecraft:knowledge_book", "Knowledge Book")
    RECORD_13 = \
        Item(2256, "minecraft:record_13", "13 Disc")
    RECORD_CAT = \
        Item(2257, "minecraft:record_cat", "Cat Disc")
    RECORD_BLOCKS = \
        Item(2258, "minecraft:record_blocks", "Blocks Disc")
    RECORD_CHIRP = \
        Item(2259, "minecraft:record_chirp", "Chirp Disc")
    RECORD_FAR = \
        Item(2260, "minecraft:record_far", "Far Disc")
    RECORD_MALL = \
        Item(2261, "minecraft:record_mall", "Mall Disc")
    RECORD_MELLOHI = \
        Item(2262, "minecraft:record_mellohi", "Mellohi Disc")
    RECORD_STAL = \
        Item(2263, "minecraft:record_stal", "Stal Disc")
    RECORD_STRAD = \
        Item(2264, "minecraft:record_strad", "Strad Disc")
    RECORD_WARD = \
        Item(2265, "minecraft:record_ward", "Ward Disc")
    RECORD_11 = \
        Item(2266, "minecraft:record_11", "11 Disc")
    RECORD_WAIT = \
        Item(2267, "minecraft:record_wait", "Wait Disc")
    ALL = {"0": AIR, "1": STONE, "1:1": STONE_1, "1:2": STONE_2, "1:3": STONE_3, "1:4": STONE_4, "1:5": STONE_5,
           "1:6": STONE_6, "2": GRASS, "3": DIRT, "3:1": DIRT_1, "3:2": DIRT_2, "4": COBBLESTONE, "5": PLANKS,
           "5:1": PLANKS_1, "5:2": PLANKS_2, "5:3": PLANKS_3, "5:4": PLANKS_4, "5:5": PLANKS_5, "6": SAPLING,
           "6:1": SAPLING_1, "6:2": SAPLING_2, "6:3": SAPLING_3, "6:4": SAPLING_4, "6:5": SAPLING_5, "7": BEDROCK,
           "8": FLOWING_WATER, "9": WATER, "10": FLOWING_LAVA, "11": LAVA, "12": SAND, "12:1": SAND_1, "13": GRAVEL,
           "14": GOLD_ORE, "15": IRON_ORE, "16": COAL_ORE, "17": LOG, "17:1": LOG_1, "17:2": LOG_2, "17:3": LOG_3,
           "18": LEAVES, "18:1": LEAVES_1, "18:2": LEAVES_2, "18:3": LEAVES_3, "19": SPONGE, "19:1": SPONGE_1,
           "20": GLASS, "21": LAPIS_ORE, "22": LAPIS_BLOCK, "23": DISPENSER, "24": SANDSTONE, "24:1": SANDSTONE_1,
           "24:2": SANDSTONE_2, "25": NOTEBLOCK, "26": BED, "27": GOLDEN_RAIL, "28": DETECTOR_RAIL, "29": STICKY_PISTON,
           "30": WEB, "31": TALLGRASS, "31:1": TALLGRASS_1, "31:2": TALLGRASS_2, "32": DEADBUSH, "33": PISTON,
           "34": PISTON_HEAD, "35": WOOL, "35:1": WOOL_1, "35:2": WOOL_2, "35:3": WOOL_3, "35:4": WOOL_4,
           "35:5": WOOL_5, "35:6": WOOL_6, "35:7": WOOL_7, "35:8": WOOL_8, "35:9": WOOL_9, "35:10": WOOL_10,
           "35:11": WOOL_11, "35:12": WOOL_12, "35:13": WOOL_13, "35:14": WOOL_14, "35:15": WOOL_15,
           "37": YELLOW_FLOWER, "38": RED_FLOWER, "38:1": RED_FLOWER_1, "38:2": RED_FLOWER_2, "38:3": RED_FLOWER_3,
           "38:4": RED_FLOWER_4, "38:5": RED_FLOWER_5, "38:6": RED_FLOWER_6, "38:7": RED_FLOWER_7, "38:8": RED_FLOWER_8,
           "39": BROWN_MUSHROOM, "40": RED_MUSHROOM, "41": GOLD_BLOCK, "42": IRON_BLOCK, "43": DOUBLE_STONE_SLAB,
           "43:1": DOUBLE_STONE_SLAB_1, "43:2": DOUBLE_STONE_SLAB_2, "43:3": DOUBLE_STONE_SLAB_3,
           "43:4": DOUBLE_STONE_SLAB_4, "43:5": DOUBLE_STONE_SLAB_5, "43:6": DOUBLE_STONE_SLAB_6,
           "43:7": DOUBLE_STONE_SLAB_7, "44": STONE_SLAB, "44:1": STONE_SLAB_1, "44:2": STONE_SLAB_2,
           "44:3": STONE_SLAB_3, "44:4": STONE_SLAB_4, "44:5": STONE_SLAB_5, "44:6": STONE_SLAB_6, "44:7": STONE_SLAB_7,
           "45": BRICK_BLOCK, "46": TNT, "47": BOOKSHELF, "48": MOSSY_COBBLESTONE, "49": OBSIDIAN, "50": TORCH,
           "51": FIRE, "52": MOB_SPAWNER, "53": OAK_STAIRS, "54": CHEST, "55": REDSTONE_WIRE, "56": DIAMOND_ORE,
           "57": DIAMOND_BLOCK, "58": CRAFTING_TABLE, "59": WHEAT, "60": FARMLAND, "61": FURNACE, "62": LIT_FURNACE,
           "63": STANDING_SIGN, "64": WOODEN_DOOR, "65": LADDER, "66": RAIL, "67": STONE_STAIRS, "68": WALL_SIGN,
           "69": LEVER, "70": STONE_PRESSURE_PLATE, "71": IRON_DOOR, "72": WOODEN_PRESSURE_PLATE, "73": REDSTONE_ORE,
           "74": LIT_REDSTONE_ORE, "75": UNLIT_REDSTONE_TORCH, "76": REDSTONE_TORCH, "77": STONE_BUTTON,
           "78": SNOW_LAYER, "79": ICE, "80": SNOW, "81": CACTUS, "82": CLAY, "83": REEDS, "84": JUKEBOX, "85": FENCE,
           "86": PUMPKIN, "87": NETHERRACK, "88": SOUL_SAND, "89": GLOWSTONE, "90": PORTAL, "91": LIT_PUMPKIN,
           "92": CAKE, "93": UNPOWERED_REPEATER, "94": POWERED_REPEATER, "95": STAINED_GLASS, "95:1": STAINED_GLASS_1,
           "95:2": STAINED_GLASS_2, "95:3": STAINED_GLASS_3, "95:4": STAINED_GLASS_4, "95:5": STAINED_GLASS_5,
           "95:6": STAINED_GLASS_6, "95:7": STAINED_GLASS_7, "95:8": STAINED_GLASS_8, "95:9": STAINED_GLASS_9,
           "95:10": STAINED_GLASS_10, "95:11": STAINED_GLASS_11, "95:12": STAINED_GLASS_12, "95:13": STAINED_GLASS_13,
           "95:14": STAINED_GLASS_14, "95:15": STAINED_GLASS_15, "96": TRAPDOOR, "97": MONSTER_EGG,
           "97:1": MONSTER_EGG_1, "97:2": MONSTER_EGG_2, "97:3": MONSTER_EGG_3, "97:4": MONSTER_EGG_4,
           "97:5": MONSTER_EGG_5, "98": STONEBRICK, "98:1": STONEBRICK_1, "98:2": STONEBRICK_2, "98:3": STONEBRICK_3,
           "99": BROWN_MUSHROOM_BLOCK, "100": RED_MUSHROOM_BLOCK, "101": IRON_BARS, "102": GLASS_PANE,
           "103": MELON_BLOCK, "104": PUMPKIN_STEM, "105": MELON_STEM, "106": VINE, "107": FENCE_GATE,
           "108": BRICK_STAIRS, "109": STONE_BRICK_STAIRS, "110": MYCELIUM, "111": WATERLILY, "112": NETHER_BRICK,
           "113": NETHER_BRICK_FENCE, "114": NETHER_BRICK_STAIRS, "115": NETHER_WART, "116": ENCHANTING_TABLE,
           "117": BREWING_STAND, "118": CAULDRON, "119": END_PORTAL, "120": END_PORTAL_FRAME, "121": END_STONE,
           "122": DRAGON_EGG, "123": REDSTONE_LAMP, "124": LIT_REDSTONE_LAMP, "125": DOUBLE_WOODEN_SLAB,
           "125:1": DOUBLE_WOODEN_SLAB_1, "125:2": DOUBLE_WOODEN_SLAB_2, "125:3": DOUBLE_WOODEN_SLAB_3,
           "125:4": DOUBLE_WOODEN_SLAB_4, "125:5": DOUBLE_WOODEN_SLAB_5, "126": WOODEN_SLAB, "126:1": WOODEN_SLAB_1,
           "126:2": WOODEN_SLAB_2, "126:3": WOODEN_SLAB_3, "126:4": WOODEN_SLAB_4, "126:5": WOODEN_SLAB_5, "127": COCOA,
           "128": SANDSTONE_STAIRS, "129": EMERALD_ORE, "130": ENDER_CHEST, "131": TRIPWIRE_HOOK, "132": TRIPWIRE_HOOK,
           "133": EMERALD_BLOCK, "134": SPRUCE_STAIRS, "135": BIRCH_STAIRS, "136": JUNGLE_STAIRS, "137": COMMAND_BLOCK,
           "138": BEACON, "139": COBBLESTONE_WALL, "139:1": COBBLESTONE_WALL_1, "140": FLOWER_POT, "141": CARROTS,
           "142": POTATOES, "143": WOODEN_BUTTON, "144": SKULL, "145": ANVIL, "146": TRAPPED_CHEST,
           "147": LIGHT_WEIGHTED_PRESSURE_PLATE, "148": HEAVY_WEIGHTED_PRESSURE_PLATE, "149": UNPOWERED_COMPARATOR,
           "150": POWERED_COMPARATOR, "151": DAYLIGHT_DETECTOR, "152": REDSTONE_BLOCK, "153": QUARTZ_ORE, "154": HOPPER,
           "155": QUARTZ_BLOCK, "155:1": QUARTZ_BLOCK_1, "155:2": QUARTZ_BLOCK_2, "156": QUARTZ_STAIRS,
           "157": ACTIVATOR_RAIL, "158": DROPPER, "159": STAINED_HARDENED_CLAY, "159:1": STAINED_HARDENED_CLAY_1,
           "159:2": STAINED_HARDENED_CLAY_2, "159:3": STAINED_HARDENED_CLAY_3, "159:4": STAINED_HARDENED_CLAY_4,
           "159:5": STAINED_HARDENED_CLAY_5, "159:6": STAINED_HARDENED_CLAY_6, "159:7": STAINED_HARDENED_CLAY_7,
           "159:8": STAINED_HARDENED_CLAY_8, "159:9": STAINED_HARDENED_CLAY_9, "159:10": STAINED_HARDENED_CLAY_10,
           "159:11": STAINED_HARDENED_CLAY_11, "159:12": STAINED_HARDENED_CLAY_12, "159:13": STAINED_HARDENED_CLAY_13,
           "159:14": STAINED_HARDENED_CLAY_14, "159:15": STAINED_HARDENED_CLAY_15, "160": STAINED_GLASS_PANE,
           "160:1": STAINED_GLASS_PANE_1, "160:2": STAINED_GLASS_PANE_2, "160:3": STAINED_GLASS_PANE_3,
           "160:4": STAINED_GLASS_PANE_4, "160:5": STAINED_GLASS_PANE_5, "160:6": STAINED_GLASS_PANE_6,
           "160:7": STAINED_GLASS_PANE_7, "160:8": STAINED_GLASS_PANE_8, "160:9": STAINED_GLASS_PANE_9,
           "160:10": STAINED_GLASS_PANE_10, "160:11": STAINED_GLASS_PANE_11, "160:12": STAINED_GLASS_PANE_12,
           "160:13": STAINED_GLASS_PANE_13, "160:14": STAINED_GLASS_PANE_14, "160:15": STAINED_GLASS_PANE_15,
           "161": LEAVES2, "161:1": LEAVES2_1, "162": LOG2, "162:1": LOG2_1, "163": ACACIA_STAIRS,
           "164": DARK_OAK_STAIRS, "165": SLIME, "166": BARRIER, "167": IRON_TRAPDOOR, "168": PRISMARINE,
           "168:1": PRISMARINE_1, "168:2": PRISMARINE_2, "169": SEA_LANTERN, "170": HAY_BLOCK, "171": CARPET,
           "171:1": CARPET_1, "171:2": CARPET_2, "171:3": CARPET_3, "171:4": CARPET_4, "171:5": CARPET_5,
           "171:6": CARPET_6, "171:7": CARPET_7, "171:8": CARPET_8, "171:9": CARPET_9, "171:10": CARPET_10,
           "171:11": CARPET_11, "171:12": CARPET_12, "171:13": CARPET_13, "171:14": CARPET_14, "171:15": CARPET_15,
           "172": HARDENED_CLAY, "173": COAL_BLOCK, "174": PACKED_ICE, "175": DOUBLE_PLANT, "175:1": DOUBLE_PLANT_1,
           "175:2": DOUBLE_PLANT_2, "175:3": DOUBLE_PLANT_3, "175:4": DOUBLE_PLANT_4, "175:5": DOUBLE_PLANT_5,
           "176": STANDING_BANNER, "177": WALL_BANNER, "178": DAYLIGHT_DETECTOR_INVERTED, "179": RED_SANDSTONE,
           "179:1": RED_SANDSTONE_1, "179:2": RED_SANDSTONE_2, "180": RED_SANDSTONE_STAIRS, "181": DOUBLE_STONE_SLAB2,
           "182": STONE_SLAB2, "183": SPRUCE_FENCE_GATE, "184": BIRCH_FENCE_GATE, "185": JUNGLE_FENCE_GATE,
           "186": DARK_OAK_FENCE_GATE, "187": ACACIA_FENCE_GATE, "188": SPRUCE_FENCE, "189": BIRCH_FENCE,
           "190": JUNGLE_FENCE, "191": DARK_OAK_FENCE, "192": ACACIA_FENCE, "193": SPRUCE_DOOR, "194": BIRCH_DOOR,
           "195": JUNGLE_DOOR, "196": ACACIA_DOOR, "197": DARK_OAK_DOOR, "198": END_ROD, "199": CHORUS_PLANT,
           "200": CHORUS_FLOWER, "201": PURPUR_BLOCK, "202": PURPUR_PILLAR, "203": PURPUR_STAIRS,
           "204": PURPUR_DOUBLE_SLAB, "205": PURPUR_SLAB, "206": END_BRICKS, "207": BEETROOTS, "208": GRASS_PATH,
           "209": END_GATEWAY, "210": REPEATING_COMMAND_BLOCK, "211": CHAIN_COMMAND_BLOCK, "212": FROSTED_ICE,
           "213": MAGMA, "214": NETHER_WART_BLOCK, "215": RED_NETHER_BRICK, "216": BONE_BLOCK, "217": STRUCTURE_VOID,
           "218": OBSERVER, "219": WHITE_SHULKER_BOX, "220": ORANGE_SHULKER_BOX, "221": MAGENTA_SHULKER_BOX,
           "222": LIGHT_BLUE_SHULKER_BOX, "223": YELLOW_SHULKER_BOX, "224": LIME_SHULKER_BOX, "225": PINK_SHULKER_BOX,
           "226": GRAY_SHULKER_BOX, "227": SILVER_SHULKER_BOX, "228": CYAN_SHULKER_BOX, "229": PURPLE_SHULKER_BOX,
           "230": BLUE_SHULKER_BOX, "231": BROWN_SHULKER_BOX, "232": GREEN_SHULKER_BOX, "233": RED_SHULKER_BOX,
           "234": BLACK_SHULKER_BOX, "235": WHITE_GLAZED_TERRACOTTA, "236": ORANGE_GLAZED_TERRACOTTA,
           "237": MAGENTA_GLAZED_TERRACOTTA, "238": LIGHT_BLUE_GLAZED_TERRACOTTA, "239": YELLOW_GLAZED_TERRACOTTA,
           "240": LIME_GLAZED_TERRACOTTA, "241": PINK_GLAZED_TERRACOTTA, "242": GRAY_GLAZED_TERRACOTTA,
           "243": LIGHT_GRAY_GLAZED_TERRACOTTA, "244": CYAN_GLAZED_TERRACOTTA, "245": PURPLE_GLAZED_TERRACOTTA,
           "246": BLUE_GLAZED_TERRACOTTA, "247": BROWN_GLAZED_TERRACOTTA, "248": GREEN_GLAZED_TERRACOTTA,
           "249": RED_GLAZED_TERRACOTTA, "250": BLACK_GLAZED_TERRACOTTA, "251": CONCRETE, "251:1": CONCRETE_1,
           "251:2": CONCRETE_2, "251:3": CONCRETE_3, "251:4": CONCRETE_4, "251:5": CONCRETE_5, "251:6": CONCRETE_6,
           "251:7": CONCRETE_7, "251:8": CONCRETE_8, "251:9": CONCRETE_9, "251:10": CONCRETE_10, "251:11": CONCRETE_11,
           "251:12": CONCRETE_12, "251:13": CONCRETE_13, "251:14": CONCRETE_14, "251:15": CONCRETE_15,
           "252": CONCRETE_POWDER, "252:1": CONCRETE_POWDER_1, "252:2": CONCRETE_POWDER_2, "252:3": CONCRETE_POWDER_3,
           "252:4": CONCRETE_POWDER_4, "252:5": CONCRETE_POWDER_5, "252:6": CONCRETE_POWDER_6,
           "252:7": CONCRETE_POWDER_7, "252:8": CONCRETE_POWDER_8, "252:9": CONCRETE_POWDER_9,
           "252:10": CONCRETE_POWDER_10, "252:11": CONCRETE_POWDER_11, "252:12": CONCRETE_POWDER_12,
           "252:13": CONCRETE_POWDER_13, "252:14": CONCRETE_POWDER_14, "252:15": CONCRETE_POWDER_15,
           "255": STRUCTURE_BLOCK, "256": IRON_SHOVEL, "257": IRON_PICKAXE, "258": IRON_AXE, "259": FLINT_AND_STEEL,
           "260": APPLE, "261": BOW, "262": ARROW, "263": COAL, "263:1": COAL_1, "264": DIAMOND, "265": IRON_INGOT,
           "266": GOLD_INGOT, "267": IRON_SWORD, "268": WOODEN_SWORD, "269": WOODEN_SHOVEL, "270": WOODEN_PICKAXE,
           "271": WOODEN_AXE, "272": STONE_SWORD, "273": STONE_SHOVEL, "274": STONE_PICKAXE, "275": STONE_AXE,
           "276": DIAMOND_SWORD, "277": DIAMOND_SHOVEL, "278": DIAMOND_PICKAXE, "279": DIAMOND_AXE, "280": STICK,
           "281": BOWL, "282": MUSHROOM_STEW, "283": GOLDEN_SWORD, "284": GOLDEN_SHOVEL, "285": GOLDEN_PICKAXE,
           "286": GOLDEN_AXE, "287": STRING, "288": FEATHER, "289": GUNPOWDER, "290": WOODEN_HOE, "291": STONE_HOE,
           "292": IRON_HOE, "293": DIAMOND_HOE, "294": GOLDEN_HOE, "295": WHEAT_SEEDS, "296": WHEAT, "297": BREAD,
           "298": LEATHER_HELMET, "299": LEATHER_CHESTPLATE, "300": LEATHER_LEGGINGS, "301": LEATHER_BOOTS,
           "302": CHAINMAIL_HELMET, "303": CHAINMAIL_CHESTPLATE, "304": CHAINMAIL_LEGGINGS, "305": CHAINMAIL_BOOTS,
           "306": IRON_HELMET, "307": IRON_CHESTPLATE, "308": IRON_LEGGINGS, "309": IRON_BOOTS, "310": DIAMOND_HELMET,
           "311": DIAMOND_CHESTPLATE, "312": DIAMOND_LEGGINGS, "313": DIAMOND_BOOTS, "314": GOLDEN_HELMET,
           "315": GOLDEN_CHESTPLATE, "316": GOLDEN_LEGGINGS, "317": GOLDEN_BOOTS, "318": FLINT, "319": PORKCHOP,
           "320": COOKED_PORKCHOP, "321": PAINTING, "322": GOLDEN_APPLE, "322:1": GOLDEN_APPLE_1, "323": SIGN,
           "324": WOODEN_DOOR, "325": BUCKET, "326": WATER_BUCKET, "327": LAVA_BUCKET, "328": MINECART, "329": SADDLE,
           "330": IRON_DOOR, "331": REDSTONE, "332": SNOWBALL, "333": BOAT, "334": LEATHER, "335": MILK_BUCKET,
           "336": BRICK, "337": CLAY_BALL, "338": REEDS, "339": PAPER, "340": BOOK, "341": SLIME_BALL,
           "342": CHEST_MINECART, "343": FURNACE_MINECART, "344": EGG, "345": COMPASS, "346": FISHING_ROD, "347": CLOCK,
           "348": GLOWSTONE_DUST, "349": FISH, "349:1": FISH_1, "349:2": FISH_2, "349:3": FISH_3, "350": COOKED_FISH,
           "350:1": COOKED_FISH_1, "351": DYE, "351:1": DYE_1, "351:2": DYE_2, "351:3": DYE_3, "351:4": DYE_4,
           "351:5": DYE_5, "351:6": DYE_6, "351:7": DYE_7, "351:8": DYE_8, "351:9": DYE_9, "351:10": DYE_10,
           "351:11": DYE_11, "351:12": DYE_12, "351:13": DYE_13, "351:14": DYE_14, "351:15": DYE_15, "352": BONE,
           "353": SUGAR, "354": CAKE, "355": BED, "356": REPEATER, "357": COOKIE, "358": FILLED_MAP, "359": SHEARS,
           "360": MELON, "361": PUMPKIN_SEEDS, "362": MELON_SEEDS, "363": BEEF, "364": COOKED_BEEF, "365": CHICKEN,
           "366": COOKED_CHICKEN, "367": ROTTEN_FLESH, "368": ENDER_PEARL, "369": BLAZE_ROD, "370": GHAST_TEAR,
           "371": GOLD_NUGGET, "372": NETHER_WART, "373": POTION, "374": GLASS_BOTTLE, "375": SPIDER_EYE,
           "376": FERMENTED_SPIDER_EYE, "377": BLAZE_POWDER, "378": MAGMA_CREAM, "379": BREWING_STAND, "380": CAULDRON,
           "381": ENDER_EYE, "382": SPECKLED_MELON, "383:4": SPAWN_EGG_4, "383:5": SPAWN_EGG_5, "383:6": SPAWN_EGG_6,
           "383:23": SPAWN_EGG_23, "383:27": SPAWN_EGG_27, "383:28": SPAWN_EGG_28, "383:29": SPAWN_EGG_29,
           "383:31": SPAWN_EGG_31, "383:32": SPAWN_EGG_32, "383:34": SPAWN_EGG_34, "383:35": SPAWN_EGG_35,
           "383:36": SPAWN_EGG_36, "383:50": SPAWN_EGG_50, "383:51": SPAWN_EGG_51, "383:52": SPAWN_EGG_52,
           "383:54": SPAWN_EGG_54, "383:55": SPAWN_EGG_55, "383:56": SPAWN_EGG_56, "383:57": SPAWN_EGG_57,
           "383:58": SPAWN_EGG_58, "383:59": SPAWN_EGG_59, "383:60": SPAWN_EGG_60, "383:61": SPAWN_EGG_61,
           "383:62": SPAWN_EGG_62, "383:65": SPAWN_EGG_65, "383:66": SPAWN_EGG_66, "383:67": SPAWN_EGG_67,
           "383:68": SPAWN_EGG_68, "383:69": SPAWN_EGG_69, "383:90": SPAWN_EGG_90, "383:91": SPAWN_EGG_91,
           "383:92": SPAWN_EGG_92, "383:93": SPAWN_EGG_93, "383:94": SPAWN_EGG_94, "383:95": SPAWN_EGG_95,
           "383:96": SPAWN_EGG_96, "383:98": SPAWN_EGG_98, "383:100": SPAWN_EGG_100, "383:101": SPAWN_EGG_101,
           "383:102": SPAWN_EGG_102, "383:103": SPAWN_EGG_103, "383:105": SPAWN_EGG_105, "383:120": SPAWN_EGG_120,
           "384": EXPERIENCE_BOTTLE, "385": FIRE_CHARGE, "386": WRITABLE_BOOK, "387": WRITTEN_BOOK, "388": EMERALD,
           "389": ITEM_FRAME, "390": FLOWER_POT, "391": CARROT, "392": POTATO, "393": BAKED_POTATO,
           "394": POISONOUS_POTATO, "395": MAP, "396": GOLDEN_CARROT, "397": SKULL, "397:1": SKULL_1, "397:2": SKULL_2,
           "397:3": SKULL_3, "397:4": SKULL_4, "397:5": SKULL_5, "398": CARROT_ON_A_STICK, "399": NETHER_STAR,
           "400": PUMPKIN_PIE, "401": FIREWORKS, "402": FIREWORK_CHARGE, "403": ENCHANTED_BOOK, "404": COMPARATOR,
           "405": NETHERBRICK, "406": QUARTZ, "407": TNT_MINECART, "408": HOPPER_MINECART, "409": PRISMARINE_SHARD,
           "410": PRISMARINE_CRYSTALS, "411": RABBIT, "412": COOKED_RABBIT, "413": RABBIT_STEW, "414": RABBIT_FOOT,
           "415": RABBIT_HIDE, "416": ARMOR_STAND, "417": IRON_HORSE_ARMOR, "418": GOLDEN_HORSE_ARMOR,
           "419": DIAMOND_HORSE_ARMOR, "420": LEAD, "421": NAME_TAG, "422": COMMAND_BLOCK_MINECART, "423": MUTTON,
           "424": COOKED_MUTTON, "425": BANNER, "426": END_CRYSTAL, "427": SPRUCE_DOOR, "428": BIRCH_DOOR,
           "429": JUNGLE_DOOR, "430": ACACIA_DOOR, "431": DARK_OAK_DOOR, "432": CHORUS_FRUIT,
           "433": POPPED_CHORUS_FRUIT, "434": BEETROOT, "435": BEETROOT_SEEDS, "436": BEETROOT_SOUP,
           "437": DRAGON_BREATH, "438": SPLASH_POTION, "439": SPECTRAL_ARROW, "440": TIPPED_ARROW,
           "441": LINGERING_POTION, "442": SHIELD, "443": ELYTRA, "444": SPRUCE_BOAT, "445": BIRCH_BOAT,
           "446": JUNGLE_BOAT, "447": ACACIA_BOAT, "448": DARK_OAK_BOAT, "449": TOTEM_OF_UNDYING, "450": SHULKER_SHELL,
           "452": IRON_NUGGET, "453": KNOWLEDGE_BOOK, "2256": RECORD_13, "2257": RECORD_CAT, "2258": RECORD_BLOCKS,
           "2259": RECORD_CHIRP, "2260": RECORD_FAR, "2261": RECORD_MALL, "2262": RECORD_MELLOHI, "2263": RECORD_STAL,
           "2264": RECORD_STRAD, "2265": RECORD_WARD, "2266": RECORD_11, "2267": RECORD_WAIT}


Items = _Items()
