from .block import Block


class _Blocks:
    def __getitem__(self, key):
        return self.ALL[key]

    AIR = \
        Block(0, 0, "minecraft:air", "Air", False, 0, False, False)
    STONE = \
        Block(1, 0, "minecraft:stone", "Stone", True, 0, False, False)
    STONE_1 = \
        Block(1, 1, "minecraft:stone_1", "Granite", True, 0, False, False)
    STONE_2 = \
        Block(1, 2, "minecraft:stone_2", "Polished Granite", True, 0, False, False)
    STONE_3 = \
        Block(1, 3, "minecraft:stone_3", "Diorite", True, 0, False, False)
    STONE_4 = \
        Block(1, 4, "minecraft:stone_4", "Polished Diorite", True, 0, False, False)
    STONE_5 = \
        Block(1, 5, "minecraft:stone_5", "Andesite", True, 0, False, False)
    STONE_6 = \
        Block(1, 6, "minecraft:stone_6", "Polished Andesite", True, 0, False, False)
    GRASS = \
        Block(2, 0, "minecraft:grass", "Grass", True, 0, False, False)
    DIRT = \
        Block(3, 0, "minecraft:dirt", "Dirt", True, 0, False, False)
    DIRT_1 = \
        Block(3, 1, "minecraft:dirt_1", "Coarse Dirt", True, 0, False, False)
    DIRT_2 = \
        Block(3, 2, "minecraft:dirt_2", "Podzol", True, 0, False, False)
    COBBLESTONE = \
        Block(4, 0, "minecraft:cobblestone", "Cobblestone", True, 0, False, False)
    PLANKS = \
        Block(5, 0, "minecraft:planks", "Oak Wood Plank", True, 0, False, False)
    PLANKS_1 = \
        Block(5, 1, "minecraft:planks_1", "Spruce Wood Plank", True, 0, False, False)
    PLANKS_2 = \
        Block(5, 2, "minecraft:planks_2", "Birch Wood Plank", True, 0, False, False)
    PLANKS_3 = \
        Block(5, 3, "minecraft:planks_3", "Jungle Wood Plank", True, 0, False, False)
    PLANKS_4 = \
        Block(5, 4, "minecraft:planks_4", "Acacia Wood Plank", True, 0, False, False)
    PLANKS_5 = \
        Block(5, 5, "minecraft:planks_5", "Dark Oak Wood Plank", True, 0, False, False)
    SAPLING = \
        Block(6, 0, "minecraft:sapling", "Oak Sapling", False, 0, False, False)
    SAPLING_1 = \
        Block(6, 1, "minecraft:sapling_1", "Spruce Sapling", False, 0, False, False)
    SAPLING_2 = \
        Block(6, 2, "minecraft:sapling_2", "Birch Sapling", False, 0, False, False)
    SAPLING_3 = \
        Block(6, 3, "minecraft:sapling_3", "Jungle Sapling", False, 0, False, False)
    SAPLING_4 = \
        Block(6, 4, "minecraft:sapling_4", "Acacia Sapling", False, 0, False, False)
    SAPLING_5 = \
        Block(6, 5, "minecraft:sapling_5", "Dark Oak Sapling", False, 0, False, False)
    BEDROCK = \
        Block(7, 0, "minecraft:bedrock", "Bedrock", True, 0, False, False)
    FLOWING_WATER = \
        Block(8, 0, "minecraft:flowing_water", "Flowing Water", True, 0, False, False)
    WATER = \
        Block(9, 0, "minecraft:water", "Still Water", True, 0, False, False)
    FLOWING_LAVA = \
        Block(10, 0, "minecraft:flowing_lava", "Flowing Lava", True, 0, False, False)
    LAVA = \
        Block(11, 0, "minecraft:lava", "Still Lava", True, 0, False, False)
    SAND = \
        Block(12, 0, "minecraft:sand", "Sand", True, 0, False, False)
    SAND_1 = \
        Block(12, 1, "minecraft:sand_1", "Red Sand", True, 0, False, False)
    GRAVEL = \
        Block(13, 0, "minecraft:gravel", "Gravel", True, 0, False, False)
    GOLD_ORE = \
        Block(14, 0, "minecraft:gold_ore", "Gold Ore", True, 0, False, False)
    IRON_ORE = \
        Block(15, 0, "minecraft:iron_ore", "Iron Ore", True, 0, False, False)
    COAL_ORE = \
        Block(16, 0, "minecraft:coal_ore", "Coal Ore", True, 0, False, False)
    LOG = \
        Block(17, 0, "minecraft:log", "Oak Wood", True, 0, False, False)
    LOG_1 = \
        Block(17, 1, "minecraft:log_1", "Spruce Wood", True, 0, False, False)
    LOG_2 = \
        Block(17, 2, "minecraft:log_2", "Birch Wood", True, 0, False, False)
    LOG_3 = \
        Block(17, 3, "minecraft:log_3", "Jungle Wood", True, 0, False, False)
    LEAVES = \
        Block(18, 0, "minecraft:leaves", "Oak Leaves", True, 0, False, False)
    LEAVES_1 = \
        Block(18, 1, "minecraft:leaves_1", "Spruce Leaves", True, 0, False, False)
    LEAVES_2 = \
        Block(18, 2, "minecraft:leaves_2", "Birch Leaves", True, 0, False, False)
    LEAVES_3 = \
        Block(18, 3, "minecraft:leaves_3", "Jungle Leaves", True, 0, False, False)
    SPONGE = \
        Block(19, 0, "minecraft:sponge", "Sponge", True, 0, False, False)
    SPONGE_1 = \
        Block(19, 1, "minecraft:sponge_1", "Wet Sponge", True, 0, False, False)
    GLASS = \
        Block(20, 0, "minecraft:glass", "Glass", True, 0, False, False)
    LAPIS_ORE = \
        Block(21, 0, "minecraft:lapis_ore", "Lapis Lazuli Ore", True, 0, False, False)
    LAPIS_BLOCK = \
        Block(22, 0, "minecraft:lapis_block", "Lapis Lazuli Block", True, 0, False, False)
    DISPENSER = \
        Block(23, 0, "minecraft:dispenser", "Dispenser", True, 0, False, False)
    SANDSTONE = \
        Block(24, 0, "minecraft:sandstone", "Sandstone", True, 0, False, False)
    SANDSTONE_1 = \
        Block(24, 1, "minecraft:sandstone_1", "Chiseled Sandstone", True, 0, False, False)
    SANDSTONE_2 = \
        Block(24, 2, "minecraft:sandstone_2", "Smooth Sandstone", True, 0, False, False)
    NOTEBLOCK = \
        Block(25, 0, "minecraft:noteblock", "Note Block", True, 0, False, False)
    BED = \
        Block(26, 0, "minecraft:bed", "Bed", False, 0, False, False)
    GOLDEN_RAIL = \
        Block(27, 0, "minecraft:golden_rail", "Powered Rail", False, 0, False, False)
    DETECTOR_RAIL = \
        Block(28, 0, "minecraft:detector_rail", "Detector Rail", False, 0, False, False)
    STICKY_PISTON = \
        Block(29, 0, "minecraft:sticky_piston", "Sticky Piston", True, 0, False, False)
    WEB = \
        Block(30, 0, "minecraft:web", "Cobweb", True, 0, False, False)
    TALLGRASS = \
        Block(31, 0, "minecraft:tallgrass", "Dead Shrub", False, 0, False, False)
    TALLGRASS_1 = \
        Block(31, 1, "minecraft:tallgrass_1", "Grass", False, 0, False, False)
    TALLGRASS_2 = \
        Block(31, 2, "minecraft:tallgrass_2", "Fern", False, 0, False, False)
    DEADBUSH = \
        Block(32, 0, "minecraft:deadbush", "Dead Bush", False, 0, False, False)
    PISTON = \
        Block(33, 0, "minecraft:piston", "Piston", True, 0, False, False)
    PISTON_HEAD = \
        Block(34, 0, "minecraft:piston_head", "Piston Head", False, 0, False, False)
    WOOL = \
        Block(35, 0, "minecraft:wool", "White Wool", True, 0, False, False)
    WOOL_1 = \
        Block(35, 1, "minecraft:wool_1", "Orange Wool", True, 0, False, False)
    WOOL_2 = \
        Block(35, 2, "minecraft:wool_2", "Magenta Wool", True, 0, False, False)
    WOOL_3 = \
        Block(35, 3, "minecraft:wool_3", "Light Blue Wool", True, 0, False, False)
    WOOL_4 = \
        Block(35, 4, "minecraft:wool_4", "Yellow Wool", True, 0, False, False)
    WOOL_5 = \
        Block(35, 5, "minecraft:wool_5", "Lime Wool", True, 0, False, False)
    WOOL_6 = \
        Block(35, 6, "minecraft:wool_6", "Pink Wool", True, 0, False, False)
    WOOL_7 = \
        Block(35, 7, "minecraft:wool_7", "Gray Wool", True, 0, False, False)
    WOOL_8 = \
        Block(35, 8, "minecraft:wool_8", "Light Gray Wool", True, 0, False, False)
    WOOL_9 = \
        Block(35, 9, "minecraft:wool_9", "Cyan Wool", True, 0, False, False)
    WOOL_10 = \
        Block(35, 10, "minecraft:wool_10", "Purple Wool", True, 0, False, False)
    WOOL_11 = \
        Block(35, 11, "minecraft:wool_11", "Blue Wool", True, 0, False, False)
    WOOL_12 = \
        Block(35, 12, "minecraft:wool_12", "Brown Wool", True, 0, False, False)
    WOOL_13 = \
        Block(35, 13, "minecraft:wool_13", "Green Wool", True, 0, False, False)
    WOOL_14 = \
        Block(35, 14, "minecraft:wool_14", "Red Wool", True, 0, False, False)
    WOOL_15 = \
        Block(35, 15, "minecraft:wool_15", "Black Wool", True, 0, False, False)
    YELLOW_FLOWER = \
        Block(37, 0, "minecraft:yellow_flower", "Dandelion", False, 0, False, False)
    RED_FLOWER = \
        Block(38, 0, "minecraft:red_flower", "Poppy", False, 0, False, False)
    RED_FLOWER_1 = \
        Block(38, 1, "minecraft:red_flower_1", "Blue Orchid", False, 0, False, False)
    RED_FLOWER_2 = \
        Block(38, 2, "minecraft:red_flower_2", "Allium", False, 0, False, False)
    RED_FLOWER_3 = \
        Block(38, 3, "minecraft:red_flower_3", "Azure Bluet", False, 0, False, False)
    RED_FLOWER_4 = \
        Block(38, 4, "minecraft:red_flower_4", "Red Tulip", False, 0, False, False)
    RED_FLOWER_5 = \
        Block(38, 5, "minecraft:red_flower_5", "Orange Tulip", False, 0, False, False)
    RED_FLOWER_6 = \
        Block(38, 6, "minecraft:red_flower_6", "White Tulip", False, 0, False, False)
    RED_FLOWER_7 = \
        Block(38, 7, "minecraft:red_flower_7", "Pink Tulip", False, 0, False, False)
    RED_FLOWER_8 = \
        Block(38, 8, "minecraft:red_flower_8", "Oxeye Daisy", False, 0, False, False)
    BROWN_MUSHROOM = \
        Block(39, 0, "minecraft:brown_mushroom", "Brown Mushroom", True, 0, False, False)
    RED_MUSHROOM = \
        Block(40, 0, "minecraft:red_mushroom", "Red Mushroom", True, 0, False, False)
    GOLD_BLOCK = \
        Block(41, 0, "minecraft:gold_block", "Gold Block", True, 0, False, False)
    IRON_BLOCK = \
        Block(42, 0, "minecraft:iron_block", "Iron Block", True, 0, False, False)
    DOUBLE_STONE_SLAB = \
        Block(43, 0, "minecraft:double_stone_slab", "Double Stone Slab", True, 0, False, False)
    DOUBLE_STONE_SLAB_1 = \
        Block(43, 1, "minecraft:double_stone_slab_1", "Double Sandstone Slab", True, 0, False, False)
    DOUBLE_STONE_SLAB_2 = \
        Block(43, 2, "minecraft:double_stone_slab_2", "Double Wooden Slab", True, 0, False, False)
    DOUBLE_STONE_SLAB_3 = \
        Block(43, 3, "minecraft:double_stone_slab_3", "Double Cobblestone Slab", True, 0, False, False)
    DOUBLE_STONE_SLAB_4 = \
        Block(43, 4, "minecraft:double_stone_slab_4", "Double Brick Slab", True, 0, False, False)
    DOUBLE_STONE_SLAB_5 = \
        Block(43, 5, "minecraft:double_stone_slab_5", "Double Stone Brick Slab", True, 0, False, False)
    DOUBLE_STONE_SLAB_6 = \
        Block(43, 6, "minecraft:double_stone_slab_6", "Double Nether Brick Slab", True, 0, False, False)
    DOUBLE_STONE_SLAB_7 = \
        Block(43, 7, "minecraft:double_stone_slab_7", "Double Quartz Slab", True, 0, False, False)
    STONE_SLAB = \
        Block(44, 0, "minecraft:stone_slab", "Stone Slab", False, 0, False, False)
    STONE_SLAB_1 = \
        Block(44, 1, "minecraft:stone_slab_1", "Sandstone Slab", False, 0, False, False)
    STONE_SLAB_2 = \
        Block(44, 2, "minecraft:stone_slab_2", "Wooden Slab", False, 0, False, False)
    STONE_SLAB_3 = \
        Block(44, 3, "minecraft:stone_slab_3", "Cobblestone Slab", False, 0, False, False)
    STONE_SLAB_4 = \
        Block(44, 4, "minecraft:stone_slab_4", "Brick Slab", False, 0, False, False)
    STONE_SLAB_5 = \
        Block(44, 5, "minecraft:stone_slab_5", "Stone Brick Slab", False, 0, False, False)
    STONE_SLAB_6 = \
        Block(44, 6, "minecraft:stone_slab_6", "Nether Brick Slab", False, 0, False, False)
    STONE_SLAB_7 = \
        Block(44, 7, "minecraft:stone_slab_7", "Quartz Slab", False, 0, False, False)
    BRICK_BLOCK = \
        Block(45, 0, "minecraft:brick_block", "Bricks", True, 0, False, False)
    TNT = \
        Block(46, 0, "minecraft:tnt", "TNT", True, 0, False, False)
    BOOKSHELF = \
        Block(47, 0, "minecraft:bookshelf", "Bookshelf", True, 0, False, False)
    MOSSY_COBBLESTONE = \
        Block(48, 0, "minecraft:mossy_cobblestone", "Moss Stone", True, 0, False, False)
    OBSIDIAN = \
        Block(49, 0, "minecraft:obsidian", "Obsidian", True, 0, False, False)
    TORCH = \
        Block(50, 0, "minecraft:torch", "Torch", False, 0, False, False)
    FIRE = \
        Block(51, 0, "minecraft:fire", "Fire", False, 0, False, False)
    MOB_SPAWNER = \
        Block(52, 0, "minecraft:mob_spawner", "Monster Spawner", True, 0, False, False)
    OAK_STAIRS = \
        Block(53, 0, "minecraft:oak_stairs", "Oak Wood Stairs", False, 0, False, False)
    CHEST = \
        Block(54, 0, "minecraft:chest", "Chest", False, 0, False, False)
    REDSTONE_WIRE = \
        Block(55, 0, "minecraft:redstone_wire", "Redstone Wire", False, 0, False, False)
    DIAMOND_ORE = \
        Block(56, 0, "minecraft:diamond_ore", "Diamond Ore", True, 0, False, False)
    DIAMOND_BLOCK = \
        Block(57, 0, "minecraft:diamond_block", "Diamond Block", True, 0, False, False)
    CRAFTING_TABLE = \
        Block(58, 0, "minecraft:crafting_table", "Crafting Table", True, 0, False, False)
    WHEAT = \
        Block(59, 0, "minecraft:wheat", "Wheat Crops", False, 0, False, False)
    FARMLAND = \
        Block(60, 0, "minecraft:farmland", "Farmland", False, 0, False, False)
    FURNACE = \
        Block(61, 0, "minecraft:furnace", "Furnace", True, 0, False, False)
    LIT_FURNACE = \
        Block(62, 0, "minecraft:lit_furnace", "Burning Furnace", True, 0, False, False)
    STANDING_SIGN = \
        Block(63, 0, "minecraft:standing_sign", "Standing Sign Block", False, 0, False, False)
    WOODEN_DOOR = \
        Block(64, 0, "minecraft:wooden_door", "Oak Door Block", False, 0, False, False)
    LADDER = \
        Block(65, 0, "minecraft:ladder", "Ladder", False, 0, False, False)
    RAIL = \
        Block(66, 0, "minecraft:rail", "Rail", False, 0, False, False)
    STONE_STAIRS = \
        Block(67, 0, "minecraft:stone_stairs", "Cobblestone Stairs", False, 0, False, False)
    WALL_SIGN = \
        Block(68, 0, "minecraft:wall_sign", "Wall-mounted Sign Block", False, 0, False, False)
    LEVER = \
        Block(69, 0, "minecraft:lever", "Lever", False, 0, False, False)
    STONE_PRESSURE_PLATE = \
        Block(70, 0, "minecraft:stone_pressure_plate", "Stone Pressure Plate", False, 0, False, False)
    IRON_DOOR = \
        Block(71, 0, "minecraft:iron_door", "Iron Door Block", False, 0, False, False)
    WOODEN_PRESSURE_PLATE = \
        Block(72, 0, "minecraft:wooden_pressure_plate", "Wooden Pressure Plate", False, 0, False, False)
    REDSTONE_ORE = \
        Block(73, 0, "minecraft:redstone_ore", "Redstone Ore", True, 0, False, False)
    LIT_REDSTONE_ORE = \
        Block(74, 0, "minecraft:lit_redstone_ore", "Glowing Redstone Ore", True, 0, False, False)
    UNLIT_REDSTONE_TORCH = \
        Block(75, 0, "minecraft:unlit_redstone_torch", "Redstone Torch (off)", False, 0, False, False)
    REDSTONE_TORCH = \
        Block(76, 0, "minecraft:redstone_torch", "Redstone Torch (on)", False, 0, False, False)
    STONE_BUTTON = \
        Block(77, 0, "minecraft:stone_button", "Stone Button", False, 0, False, False)
    SNOW_LAYER = \
        Block(78, 0, "minecraft:snow_layer", "Snow", False, 0, False, False)
    ICE = \
        Block(79, 0, "minecraft:ice", "Ice", True, 0, False, False)
    SNOW = \
        Block(80, 0, "minecraft:snow", "Snow Block", True, 0, False, False)
    CACTUS = \
        Block(81, 0, "minecraft:cactus", "Cactus", False, 0, False, False)
    CLAY = \
        Block(82, 0, "minecraft:clay", "Clay", True, 0, False, False)
    REEDS = \
        Block(83, 0, "minecraft:reeds", "Sugar Canes", False, 0, False, False)
    JUKEBOX = \
        Block(84, 0, "minecraft:jukebox", "Jukebox", True, 0, False, False)
    FENCE = \
        Block(85, 0, "minecraft:fence", "Oak Fence", False, 0, False, False)
    PUMPKIN = \
        Block(86, 0, "minecraft:pumpkin", "Pumpkin", True, 0, False, False)
    NETHERRACK = \
        Block(87, 0, "minecraft:netherrack", "Netherrack", True, 0, False, False)
    SOUL_SAND = \
        Block(88, 0, "minecraft:soul_sand", "Soul Sand", False, 0, False, False)
    GLOWSTONE = \
        Block(89, 0, "minecraft:glowstone", "Glowstone", True, 0, False, False)
    PORTAL = \
        Block(90, 0, "minecraft:portal", "Nether Portal", True, 0, False, False)
    LIT_PUMPKIN = \
        Block(91, 0, "minecraft:lit_pumpkin", "Jack o'Lantern", True, 0, False, False)
    CAKE = \
        Block(92, 0, "minecraft:cake", "Cake Block", False, 0, False, False)
    UNPOWERED_REPEATER = \
        Block(93, 0, "minecraft:unpowered_repeater", "Redstone Repeater Block (off)", False, 0, False, False)
    POWERED_REPEATER = \
        Block(94, 0, "minecraft:powered_repeater", "Redstone Repeater Block (on)", False, 0, False, False)
    STAINED_GLASS = \
        Block(95, 0, "minecraft:stained_glass", "White Stained Glass", False, 0, False, False)
    STAINED_GLASS_1 = \
        Block(95, 1, "minecraft:stained_glass_1", "Orange Stained Glass", False, 0, False, False)
    STAINED_GLASS_2 = \
        Block(95, 2, "minecraft:stained_glass_2", "Magenta Stained Glass", False, 0, False, False)
    STAINED_GLASS_3 = \
        Block(95, 3, "minecraft:stained_glass_3", "Light Blue Stained Glass", False, 0, False, False)
    STAINED_GLASS_4 = \
        Block(95, 4, "minecraft:stained_glass_4", "Yellow Stained Glass", False, 0, False, False)
    STAINED_GLASS_5 = \
        Block(95, 5, "minecraft:stained_glass_5", "Lime Stained Glass", False, 0, False, False)
    STAINED_GLASS_6 = \
        Block(95, 6, "minecraft:stained_glass_6", "Pink Stained Glass", False, 0, False, False)
    STAINED_GLASS_7 = \
        Block(95, 7, "minecraft:stained_glass_7", "Gray Stained Glass", False, 0, False, False)
    STAINED_GLASS_8 = \
        Block(95, 8, "minecraft:stained_glass_8", "Light Gray Stained Glass", False, 0, False, False)
    STAINED_GLASS_9 = \
        Block(95, 9, "minecraft:stained_glass_9", "Cyan Stained Glass", False, 0, False, False)
    STAINED_GLASS_10 = \
        Block(95, 10, "minecraft:stained_glass_10", "Purple Stained Glass", False, 0, False, False)
    STAINED_GLASS_11 = \
        Block(95, 11, "minecraft:stained_glass_11", "Blue Stained Glass", False, 0, False, False)
    STAINED_GLASS_12 = \
        Block(95, 12, "minecraft:stained_glass_12", "Brown Stained Glass", False, 0, False, False)
    STAINED_GLASS_13 = \
        Block(95, 13, "minecraft:stained_glass_13", "Green Stained Glass", False, 0, False, False)
    STAINED_GLASS_14 = \
        Block(95, 14, "minecraft:stained_glass_14", "Red Stained Glass", False, 0, False, False)
    STAINED_GLASS_15 = \
        Block(95, 15, "minecraft:stained_glass_15", "Black Stained Glass", False, 0, False, False)
    TRAPDOOR = \
        Block(96, 0, "minecraft:trapdoor", "Wooden Trapdoor", False, 0, False, False)
    MONSTER_EGG = \
        Block(97, 0, "minecraft:monster_egg", "Stone Monster Egg", True, 0, False, False)
    MONSTER_EGG_1 = \
        Block(97, 1, "minecraft:monster_egg_1", "Cobblestone Monster Egg", True, 0, False, False)
    MONSTER_EGG_2 = \
        Block(97, 2, "minecraft:monster_egg_2", "Stone Brick Monster Egg", True, 0, False, False)
    MONSTER_EGG_3 = \
        Block(97, 3, "minecraft:monster_egg_3", "Mossy Stone Brick Monster Egg", True, 0, False, False)
    MONSTER_EGG_4 = \
        Block(97, 4, "minecraft:monster_egg_4", "Cracked Stone Brick Monster Egg", True, 0, False, False)
    MONSTER_EGG_5 = \
        Block(97, 5, "minecraft:monster_egg_5", "Chiseled Stone Brick Monster Egg", True, 0, False, False)
    STONEBRICK = \
        Block(98, 0, "minecraft:stonebrick", "Stone Bricks", True, 0, False, False)
    STONEBRICK_1 = \
        Block(98, 1, "minecraft:stonebrick_1", "Mossy Stone Bricks", True, 0, False, False)
    STONEBRICK_2 = \
        Block(98, 2, "minecraft:stonebrick_2", "Cracked Stone Bricks", True, 0, False, False)
    STONEBRICK_3 = \
        Block(98, 3, "minecraft:stonebrick_3", "Chiseled Stone Bricks", True, 0, False, False)
    BROWN_MUSHROOM_BLOCK = \
        Block(99, 0, "minecraft:brown_mushroom_block", "Brown Mushroom Block", True, 0, False, False)
    RED_MUSHROOM_BLOCK = \
        Block(100, 0, "minecraft:red_mushroom_block", "Red Mushroom Block", True, 0, False, False)
    IRON_BARS = \
        Block(101, 0, "minecraft:iron_bars", "Iron Bars", False, 0, False, False)
    GLASS_PANE = \
        Block(102, 0, "minecraft:glass_pane", "Glass Pane", False, 0, False, False)
    MELON_BLOCK = \
        Block(103, 0, "minecraft:melon_block", "Melon Block", True, 0, False, False)
    PUMPKIN_STEM = \
        Block(104, 0, "minecraft:pumpkin_stem", "Pumpkin Stem", False, 0, False, False)
    MELON_STEM = \
        Block(105, 0, "minecraft:melon_stem", "Melon Stem", False, 0, False, False)
    VINE = \
        Block(106, 0, "minecraft:vine", "Vines", False, 0, False, False)
    FENCE_GATE = \
        Block(107, 0, "minecraft:fence_gate", "Oak Fence Gate", False, 0, False, False)
    BRICK_STAIRS = \
        Block(108, 0, "minecraft:brick_stairs", "Brick Stairs", False, 0, False, False)
    STONE_BRICK_STAIRS = \
        Block(109, 0, "minecraft:stone_brick_stairs", "Stone Brick Stairs", False, 0, False, False)
    MYCELIUM = \
        Block(110, 0, "minecraft:mycelium", "Mycelium", True, 0, False, False)
    WATERLILY = \
        Block(111, 0, "minecraft:waterlily", "Lily Pad", False, 0, False, False)
    NETHER_BRICK = \
        Block(112, 0, "minecraft:nether_brick", "Nether Brick", True, 0, False, False)
    NETHER_BRICK_FENCE = \
        Block(113, 0, "minecraft:nether_brick_fence", "Nether Brick Fence", False, 0, False, False)
    NETHER_BRICK_STAIRS = \
        Block(114, 0, "minecraft:nether_brick_stairs", "Nether Brick Stairs", False, 0, False, False)
    NETHER_WART = \
        Block(115, 0, "minecraft:nether_wart", "Nether Wart", False, 0, False, False)
    ENCHANTING_TABLE = \
        Block(116, 0, "minecraft:enchanting_table", "Enchantment Table", False, 0, False, False)
    BREWING_STAND = \
        Block(117, 0, "minecraft:brewing_stand", "Brewing Stand", False, 0, False, False)
    CAULDRON = \
        Block(118, 0, "minecraft:cauldron", "Cauldron", False, 0, False, False)
    END_PORTAL = \
        Block(119, 0, "minecraft:end_portal", "End Portal", True, 0, False, False)
    END_PORTAL_FRAME = \
        Block(120, 0, "minecraft:end_portal_frame", "End Portal Frame", False, 0, False, False)
    END_STONE = \
        Block(121, 0, "minecraft:end_stone", "End Stone", True, 0, False, False)
    DRAGON_EGG = \
        Block(122, 0, "minecraft:dragon_egg", "Dragon Egg", False, 0, False, False)
    REDSTONE_LAMP = \
        Block(123, 0, "minecraft:redstone_lamp", "Redstone Lamp (inactive)", True, 0, False, False)
    LIT_REDSTONE_LAMP = \
        Block(124, 0, "minecraft:lit_redstone_lamp", "Redstone Lamp (active)", True, 0, False, False)
    DOUBLE_WOODEN_SLAB = \
        Block(125, 0, "minecraft:double_wooden_slab", "Double Oak Wood Slab", True, 0, False, False)
    DOUBLE_WOODEN_SLAB_1 = \
        Block(125, 1, "minecraft:double_wooden_slab_1", "Double Spruce Wood Slab", True, 0, False, False)
    DOUBLE_WOODEN_SLAB_2 = \
        Block(125, 2, "minecraft:double_wooden_slab_2", "Double Birch Wood Slab", True, 0, False, False)
    DOUBLE_WOODEN_SLAB_3 = \
        Block(125, 3, "minecraft:double_wooden_slab_3", "Double Jungle Wood Slab", True, 0, False, False)
    DOUBLE_WOODEN_SLAB_4 = \
        Block(125, 4, "minecraft:double_wooden_slab_4", "Double Acacia Wood Slab", True, 0, False, False)
    DOUBLE_WOODEN_SLAB_5 = \
        Block(125, 5, "minecraft:double_wooden_slab_5", "Double Dark Oak Wood Slab", True, 0, False, False)
    WOODEN_SLAB = \
        Block(126, 0, "minecraft:wooden_slab", "Oak Wood Slab", False, 0, False, False)
    WOODEN_SLAB_1 = \
        Block(126, 1, "minecraft:wooden_slab_1", "Spruce Wood Slab", False, 0, False, False)
    WOODEN_SLAB_2 = \
        Block(126, 2, "minecraft:wooden_slab_2", "Birch Wood Slab", False, 0, False, False)
    WOODEN_SLAB_3 = \
        Block(126, 3, "minecraft:wooden_slab_3", "Jungle Wood Slab", False, 0, False, False)
    WOODEN_SLAB_4 = \
        Block(126, 4, "minecraft:wooden_slab_4", "Acacia Wood Slab", False, 0, False, False)
    WOODEN_SLAB_5 = \
        Block(126, 5, "minecraft:wooden_slab_5", "Dark Oak Wood Slab", False, 0, False, False)
    COCOA = \
        Block(127, 0, "minecraft:cocoa", "Cocoa", True, 0, False, False)
    SANDSTONE_STAIRS = \
        Block(128, 0, "minecraft:sandstone_stairs", "Sandstone Stairs", False, 0, False, False)
    EMERALD_ORE = \
        Block(129, 0, "minecraft:emerald_ore", "Emerald Ore", True, 0, False, False)
    ENDER_CHEST = \
        Block(130, 0, "minecraft:ender_chest", "Ender Chest", False, 0, False, False)
    TRIPWIRE_HOOK = \
        Block(131, 0, "minecraft:tripwire_hook", "Tripwire Hook", False, 0, False, False)
    TRIPWIRE_HOOK = \
        Block(132, 0, "minecraft:tripwire_hook", "Tripwire", False, 0, False, False)
    EMERALD_BLOCK = \
        Block(133, 0, "minecraft:emerald_block", "Emerald Block", True, 0, False, False)
    SPRUCE_STAIRS = \
        Block(134, 0, "minecraft:spruce_stairs", "Spruce Wood Stairs", False, 0, False, False)
    BIRCH_STAIRS = \
        Block(135, 0, "minecraft:birch_stairs", "Birch Wood Stairs", False, 0, False, False)
    JUNGLE_STAIRS = \
        Block(136, 0, "minecraft:jungle_stairs", "Jungle Wood Stairs", False, 0, False, False)
    COMMAND_BLOCK = \
        Block(137, 0, "minecraft:command_block", "Command Block", True, 0, False, False)
    BEACON = \
        Block(138, 0, "minecraft:beacon", "Beacon", True, 0, False, False)
    COBBLESTONE_WALL = \
        Block(139, 0, "minecraft:cobblestone_wall", "Cobblestone Wall", False, 0, False, False)
    COBBLESTONE_WALL_1 = \
        Block(139, 1, "minecraft:cobblestone_wall_1", "Mossy Cobblestone Wall", False, 0, False, False)
    FLOWER_POT = \
        Block(140, 0, "minecraft:flower_pot", "Flower Pot", False, 0, False, False)
    CARROTS = \
        Block(141, 0, "minecraft:carrots", "Carrots", False, 0, False, False)
    POTATOES = \
        Block(142, 0, "minecraft:potatoes", "Potatoes", False, 0, False, False)
    WOODEN_BUTTON = \
        Block(143, 0, "minecraft:wooden_button", "Wooden Button", False, 0, False, False)
    SKULL = \
        Block(144, 0, "minecraft:skull", "Mob Head", False, 0, False, False)
    ANVIL = \
        Block(145, 0, "minecraft:anvil", "Anvil", False, 0, False, False)
    TRAPPED_CHEST = \
        Block(146, 0, "minecraft:trapped_chest", "Trapped Chest", False, 0, False, False)
    LIGHT_WEIGHTED_PRESSURE_PLATE = \
        Block(147, 0, "minecraft:light_weighted_pressure_plate", "Weighted Pressure Plate (light)", False, 0, False,
              False)
    HEAVY_WEIGHTED_PRESSURE_PLATE = \
        Block(148, 0, "minecraft:heavy_weighted_pressure_plate", "Weighted Pressure Plate (heavy)", False, 0, False,
              False)
    UNPOWERED_COMPARATOR = \
        Block(149, 0, "minecraft:unpowered_comparator", "Redstone Comparator (inactive)", False, 0, False, False)
    POWERED_COMPARATOR = \
        Block(150, 0, "minecraft:powered_comparator", "Redstone Comparator (active)", False, 0, False, False)
    DAYLIGHT_DETECTOR = \
        Block(151, 0, "minecraft:daylight_detector", "Daylight Sensor", False, 0, False, False)
    REDSTONE_BLOCK = \
        Block(152, 0, "minecraft:redstone_block", "Redstone Block", True, 0, False, False)
    QUARTZ_ORE = \
        Block(153, 0, "minecraft:quartz_ore", "Nether Quartz Ore", True, 0, False, False)
    HOPPER = \
        Block(154, 0, "minecraft:hopper", "Hopper", True, 0, False, False)
    QUARTZ_BLOCK = \
        Block(155, 0, "minecraft:quartz_block", "Quartz Block", True, 0, False, False)
    QUARTZ_BLOCK_1 = \
        Block(155, 1, "minecraft:quartz_block_1", "Chiseled Quartz Block", True, 0, False, False)
    QUARTZ_BLOCK_2 = \
        Block(155, 2, "minecraft:quartz_block_2", "Pillar Quartz Block", True, 0, False, False)
    QUARTZ_STAIRS = \
        Block(156, 0, "minecraft:quartz_stairs", "Quartz Stairs", False, 0, False, False)
    ACTIVATOR_RAIL = \
        Block(157, 0, "minecraft:activator_rail", "Activator Rail", False, 0, False, False)
    DROPPER = \
        Block(158, 0, "minecraft:dropper", "Dropper", True, 0, False, False)
    STAINED_HARDENED_CLAY = \
        Block(159, 0, "minecraft:stained_hardened_clay", "White Hardened Clay", True, 0, False, False)
    STAINED_HARDENED_CLAY_1 = \
        Block(159, 1, "minecraft:stained_hardened_clay_1", "Orange Hardened Clay", True, 0, False, False)
    STAINED_HARDENED_CLAY_2 = \
        Block(159, 2, "minecraft:stained_hardened_clay_2", "Magenta Hardened Clay", True, 0, False, False)
    STAINED_HARDENED_CLAY_3 = \
        Block(159, 3, "minecraft:stained_hardened_clay_3", "Light Blue Hardened Clay", True, 0, False, False)
    STAINED_HARDENED_CLAY_4 = \
        Block(159, 4, "minecraft:stained_hardened_clay_4", "Yellow Hardened Clay", True, 0, False, False)
    STAINED_HARDENED_CLAY_5 = \
        Block(159, 5, "minecraft:stained_hardened_clay_5", "Lime Hardened Clay", True, 0, False, False)
    STAINED_HARDENED_CLAY_6 = \
        Block(159, 6, "minecraft:stained_hardened_clay_6", "Pink Hardened Clay", True, 0, False, False)
    STAINED_HARDENED_CLAY_7 = \
        Block(159, 7, "minecraft:stained_hardened_clay_7", "Gray Hardened Clay", True, 0, False, False)
    STAINED_HARDENED_CLAY_8 = \
        Block(159, 8, "minecraft:stained_hardened_clay_8", "Light Gray Hardened Clay", True, 0, False, False)
    STAINED_HARDENED_CLAY_9 = \
        Block(159, 9, "minecraft:stained_hardened_clay_9", "Cyan Hardened Clay", True, 0, False, False)
    STAINED_HARDENED_CLAY_10 = \
        Block(159, 10, "minecraft:stained_hardened_clay_10", "Purple Hardened Clay", True, 0, False, False)
    STAINED_HARDENED_CLAY_11 = \
        Block(159, 11, "minecraft:stained_hardened_clay_11", "Blue Hardened Clay", True, 0, False, False)
    STAINED_HARDENED_CLAY_12 = \
        Block(159, 12, "minecraft:stained_hardened_clay_12", "Brown Hardened Clay", True, 0, False, False)
    STAINED_HARDENED_CLAY_13 = \
        Block(159, 13, "minecraft:stained_hardened_clay_13", "Green Hardened Clay", True, 0, False, False)
    STAINED_HARDENED_CLAY_14 = \
        Block(159, 14, "minecraft:stained_hardened_clay_14", "Red Hardened Clay", True, 0, False, False)
    STAINED_HARDENED_CLAY_15 = \
        Block(159, 15, "minecraft:stained_hardened_clay_15", "Black Hardened Clay", True, 0, False, False)
    STAINED_GLASS_PANE = \
        Block(160, 0, "minecraft:stained_glass_pane", "White Stained Glass Pane", False, 0, False, False)
    STAINED_GLASS_PANE_1 = \
        Block(160, 1, "minecraft:stained_glass_pane_1", "Orange Stained Glass Pane", False, 0, False, False)
    STAINED_GLASS_PANE_2 = \
        Block(160, 2, "minecraft:stained_glass_pane_2", "Magenta Stained Glass Pane", False, 0, False, False)
    STAINED_GLASS_PANE_3 = \
        Block(160, 3, "minecraft:stained_glass_pane_3", "Light Blue Stained Glass Pane", False, 0, False, False)
    STAINED_GLASS_PANE_4 = \
        Block(160, 4, "minecraft:stained_glass_pane_4", "Yellow Stained Glass Pane", False, 0, False, False)
    STAINED_GLASS_PANE_5 = \
        Block(160, 5, "minecraft:stained_glass_pane_5", "Lime Stained Glass Pane", False, 0, False, False)
    STAINED_GLASS_PANE_6 = \
        Block(160, 6, "minecraft:stained_glass_pane_6", "Pink Stained Glass Pane", False, 0, False, False)
    STAINED_GLASS_PANE_7 = \
        Block(160, 7, "minecraft:stained_glass_pane_7", "Gray Stained Glass Pane", False, 0, False, False)
    STAINED_GLASS_PANE_8 = \
        Block(160, 8, "minecraft:stained_glass_pane_8", "Light Gray Stained Glass Pane", False, 0, False, False)
    STAINED_GLASS_PANE_9 = \
        Block(160, 9, "minecraft:stained_glass_pane_9", "Cyan Stained Glass Pane", False, 0, False, False)
    STAINED_GLASS_PANE_10 = \
        Block(160, 10, "minecraft:stained_glass_pane_10", "Purple Stained Glass Pane", False, 0, False, False)
    STAINED_GLASS_PANE_11 = \
        Block(160, 11, "minecraft:stained_glass_pane_11", "Blue Stained Glass Pane", False, 0, False, False)
    STAINED_GLASS_PANE_12 = \
        Block(160, 12, "minecraft:stained_glass_pane_12", "Brown Stained Glass Pane", False, 0, False, False)
    STAINED_GLASS_PANE_13 = \
        Block(160, 13, "minecraft:stained_glass_pane_13", "Green Stained Glass Pane", False, 0, False, False)
    STAINED_GLASS_PANE_14 = \
        Block(160, 14, "minecraft:stained_glass_pane_14", "Red Stained Glass Pane", False, 0, False, False)
    STAINED_GLASS_PANE_15 = \
        Block(160, 15, "minecraft:stained_glass_pane_15", "Black Stained Glass Pane", False, 0, False, False)
    LEAVES2 = \
        Block(161, 0, "minecraft:leaves2", "Acacia Leaves", True, 0, False, False)
    LEAVES2_1 = \
        Block(161, 1, "minecraft:leaves2_1", "Dark Oak Leaves", True, 0, False, False)
    LOG2 = \
        Block(162, 0, "minecraft:log2", "Acacia Wood", True, 0, False, False)
    LOG2_1 = \
        Block(162, 1, "minecraft:log2_1", "Dark Oak Wood", True, 0, False, False)
    ACACIA_STAIRS = \
        Block(163, 0, "minecraft:acacia_stairs", "Acacia Wood Stairs", False, 0, False, False)
    DARK_OAK_STAIRS = \
        Block(164, 0, "minecraft:dark_oak_stairs", "Dark Oak Wood Stairs", False, 0, False, False)
    SLIME = \
        Block(165, 0, "minecraft:slime", "Slime Block", True, 0, False, False)
    BARRIER = \
        Block(166, 0, "minecraft:barrier", "Barrier", True, 0, False, False)
    IRON_TRAPDOOR = \
        Block(167, 0, "minecraft:iron_trapdoor", "Iron Trapdoor", False, 0, False, False)
    PRISMARINE = \
        Block(168, 0, "minecraft:prismarine", "Prismarine", True, 0, False, False)
    PRISMARINE_1 = \
        Block(168, 1, "minecraft:prismarine_1", "Prismarine Bricks", True, 0, False, False)
    PRISMARINE_2 = \
        Block(168, 2, "minecraft:prismarine_2", "Dark Prismarine", True, 0, False, False)
    SEA_LANTERN = \
        Block(169, 0, "minecraft:sea_lantern", "Sea Lantern", True, 0, False, False)
    HAY_BLOCK = \
        Block(170, 0, "minecraft:hay_block", "Hay Bale", True, 0, False, False)
    CARPET = \
        Block(171, 0, "minecraft:carpet", "White Carpet", False, 0, False, False)
    CARPET_1 = \
        Block(171, 1, "minecraft:carpet_1", "Orange Carpet", False, 0, False, False)
    CARPET_2 = \
        Block(171, 2, "minecraft:carpet_2", "Magenta Carpet", False, 0, False, False)
    CARPET_3 = \
        Block(171, 3, "minecraft:carpet_3", "Light Blue Carpet", False, 0, False, False)
    CARPET_4 = \
        Block(171, 4, "minecraft:carpet_4", "Yellow Carpet", False, 0, False, False)
    CARPET_5 = \
        Block(171, 5, "minecraft:carpet_5", "Lime Carpet", False, 0, False, False)
    CARPET_6 = \
        Block(171, 6, "minecraft:carpet_6", "Pink Carpet", False, 0, False, False)
    CARPET_7 = \
        Block(171, 7, "minecraft:carpet_7", "Gray Carpet", False, 0, False, False)
    CARPET_8 = \
        Block(171, 8, "minecraft:carpet_8", "Light Gray Carpet", False, 0, False, False)
    CARPET_9 = \
        Block(171, 9, "minecraft:carpet_9", "Cyan Carpet", False, 0, False, False)
    CARPET_10 = \
        Block(171, 10, "minecraft:carpet_10", "Purple Carpet", False, 0, False, False)
    CARPET_11 = \
        Block(171, 11, "minecraft:carpet_11", "Blue Carpet", False, 0, False, False)
    CARPET_12 = \
        Block(171, 12, "minecraft:carpet_12", "Brown Carpet", False, 0, False, False)
    CARPET_13 = \
        Block(171, 13, "minecraft:carpet_13", "Green Carpet", False, 0, False, False)
    CARPET_14 = \
        Block(171, 14, "minecraft:carpet_14", "Red Carpet", False, 0, False, False)
    CARPET_15 = \
        Block(171, 15, "minecraft:carpet_15", "Black Carpet", False, 0, False, False)
    HARDENED_CLAY = \
        Block(172, 0, "minecraft:hardened_clay", "Hardened Clay", True, 0, False, False)
    COAL_BLOCK = \
        Block(173, 0, "minecraft:coal_block", "Block of Coal", True, 0, False, False)
    PACKED_ICE = \
        Block(174, 0, "minecraft:packed_ice", "Packed Ice", True, 0, False, False)
    DOUBLE_PLANT = \
        Block(175, 0, "minecraft:double_plant", "Sunflower", False, 0, False, False)
    DOUBLE_PLANT_1 = \
        Block(175, 1, "minecraft:double_plant_1", "Lilac", False, 0, False, False)
    DOUBLE_PLANT_2 = \
        Block(175, 2, "minecraft:double_plant_2", "Double Tallgrass", False, 0, False, False)
    DOUBLE_PLANT_3 = \
        Block(175, 3, "minecraft:double_plant_3", "Large Fern", False, 0, False, False)
    DOUBLE_PLANT_4 = \
        Block(175, 4, "minecraft:double_plant_4", "Rose Bush", False, 0, False, False)
    DOUBLE_PLANT_5 = \
        Block(175, 5, "minecraft:double_plant_5", "Peony", False, 0, False, False)
    STANDING_BANNER = \
        Block(176, 0, "minecraft:standing_banner", "Free-standing Banner", False, 0, False, False)
    WALL_BANNER = \
        Block(177, 0, "minecraft:wall_banner", "Wall-mounted Banner", False, 0, False, False)
    DAYLIGHT_DETECTOR_INVERTED = \
        Block(178, 0, "minecraft:daylight_detector_inverted", "Inverted Daylight Sensor", False, 0, False, False)
    RED_SANDSTONE = \
        Block(179, 0, "minecraft:red_sandstone", "Red Sandstone", True, 0, False, False)
    RED_SANDSTONE_1 = \
        Block(179, 1, "minecraft:red_sandstone_1", "Chiseled Red Sandstone", True, 0, False, False)
    RED_SANDSTONE_2 = \
        Block(179, 2, "minecraft:red_sandstone_2", "Smooth Red Sandstone", True, 0, False, False)
    RED_SANDSTONE_STAIRS = \
        Block(180, 0, "minecraft:red_sandstone_stairs", "Red Sandstone Stairs", False, 0, False, False)
    DOUBLE_STONE_SLAB2 = \
        Block(181, 0, "minecraft:double_stone_slab2", "Double Red Sandstone Slab", True, 0, False, False)
    STONE_SLAB2 = \
        Block(182, 0, "minecraft:stone_slab2", "Red Sandstone Slab", False, 0, False, False)
    SPRUCE_FENCE_GATE = \
        Block(183, 0, "minecraft:spruce_fence_gate", "Spruce Fence Gate", False, 0, False, False)
    BIRCH_FENCE_GATE = \
        Block(184, 0, "minecraft:birch_fence_gate", "Birch Fence Gate", False, 0, False, False)
    JUNGLE_FENCE_GATE = \
        Block(185, 0, "minecraft:jungle_fence_gate", "Jungle Fence Gate", False, 0, False, False)
    DARK_OAK_FENCE_GATE = \
        Block(186, 0, "minecraft:dark_oak_fence_gate", "Dark Oak Fence Gate", False, 0, False, False)
    ACACIA_FENCE_GATE = \
        Block(187, 0, "minecraft:acacia_fence_gate", "Acacia Fence Gate", False, 0, False, False)
    SPRUCE_FENCE = \
        Block(188, 0, "minecraft:spruce_fence", "Spruce Fence", False, 0, False, False)
    BIRCH_FENCE = \
        Block(189, 0, "minecraft:birch_fence", "Birch Fence", False, 0, False, False)
    JUNGLE_FENCE = \
        Block(190, 0, "minecraft:jungle_fence", "Jungle Fence", False, 0, False, False)
    DARK_OAK_FENCE = \
        Block(191, 0, "minecraft:dark_oak_fence", "Dark Oak Fence", False, 0, False, False)
    ACACIA_FENCE = \
        Block(192, 0, "minecraft:acacia_fence", "Acacia Fence", False, 0, False, False)
    SPRUCE_DOOR = \
        Block(193, 0, "minecraft:spruce_door", "Spruce Door Block", False, 0, False, False)
    BIRCH_DOOR = \
        Block(194, 0, "minecraft:birch_door", "Birch Door Block", False, 0, False, False)
    JUNGLE_DOOR = \
        Block(195, 0, "minecraft:jungle_door", "Jungle Door Block", False, 0, False, False)
    ACACIA_DOOR = \
        Block(196, 0, "minecraft:acacia_door", "Acacia Door Block", False, 0, False, False)
    DARK_OAK_DOOR = \
        Block(197, 0, "minecraft:dark_oak_door", "Dark Oak Door Block", False, 0, False, False)
    END_ROD = \
        Block(198, 0, "minecraft:end_rod", "End Rod", False, 0, False, False)
    CHORUS_PLANT = \
        Block(199, 0, "minecraft:chorus_plant", "Chorus Plant", False, 0, False, False)
    CHORUS_FLOWER = \
        Block(200, 0, "minecraft:chorus_flower", "Chorus Flower", False, 0, False, False)
    PURPUR_BLOCK = \
        Block(201, 0, "minecraft:purpur_block", "Purpur Block", True, 0, False, False)
    PURPUR_PILLAR = \
        Block(202, 0, "minecraft:purpur_pillar", "Purpur Pillar", True, 0, False, False)
    PURPUR_STAIRS = \
        Block(203, 0, "minecraft:purpur_stairs", "Purpur Stairs", False, 0, False, False)
    PURPUR_DOUBLE_SLAB = \
        Block(204, 0, "minecraft:purpur_double_slab", "Purpur Double Slab", True, 0, False, False)
    PURPUR_SLAB = \
        Block(205, 0, "minecraft:purpur_slab", "Purpur Slab", False, 0, False, False)
    END_BRICKS = \
        Block(206, 0, "minecraft:end_bricks", "End Stone Bricks", True, 0, False, False)
    BEETROOTS = \
        Block(207, 0, "minecraft:beetroots", "Beetroot Block", True, 0, False, False)
    GRASS_PATH = \
        Block(208, 0, "minecraft:grass_path", "Grass Path", True, 0, False, False)
    END_GATEWAY = \
        Block(209, 0, "minecraft:end_gateway", "End Gateway", True, 0, False, False)
    REPEATING_COMMAND_BLOCK = \
        Block(210, 0, "minecraft:repeating_command_block", "Repeating Command Block", True, 0, False, False)
    CHAIN_COMMAND_BLOCK = \
        Block(211, 0, "minecraft:chain_command_block", "Chain Command Block", True, 0, False, False)
    FROSTED_ICE = \
        Block(212, 0, "minecraft:frosted_ice", "Frosted Ice", True, 0, False, False)
    MAGMA = \
        Block(213, 0, "minecraft:magma", "Magma Block", True, 0, False, False)
    NETHER_WART_BLOCK = \
        Block(214, 0, "minecraft:nether_wart_block", "Nether Wart Block", True, 0, False, False)
    RED_NETHER_BRICK = \
        Block(215, 0, "minecraft:red_nether_brick", "Red Nether Brick", True, 0, False, False)
    BONE_BLOCK = \
        Block(216, 0, "minecraft:bone_block", "Bone Block", True, 0, False, False)
    STRUCTURE_VOID = \
        Block(217, 0, "minecraft:structure_void", "Structure Void", True, 0, False, False)
    OBSERVER = \
        Block(218, 0, "minecraft:observer", "Observer", True, 0, False, False)
    WHITE_SHULKER_BOX = \
        Block(219, 0, "minecraft:white_shulker_box", "White Shulker Box", True, 0, False, False)
    ORANGE_SHULKER_BOX = \
        Block(220, 0, "minecraft:orange_shulker_box", "Orange Shulker Box", True, 0, False, False)
    MAGENTA_SHULKER_BOX = \
        Block(221, 0, "minecraft:magenta_shulker_box", "Magenta Shulker Box", True, 0, False, False)
    LIGHT_BLUE_SHULKER_BOX = \
        Block(222, 0, "minecraft:light_blue_shulker_box", "Light Blue Shulker Box", True, 0, False, False)
    YELLOW_SHULKER_BOX = \
        Block(223, 0, "minecraft:yellow_shulker_box", "Yellow Shulker Box", True, 0, False, False)
    LIME_SHULKER_BOX = \
        Block(224, 0, "minecraft:lime_shulker_box", "Lime Shulker Box", True, 0, False, False)
    PINK_SHULKER_BOX = \
        Block(225, 0, "minecraft:pink_shulker_box", "Pink Shulker Box", True, 0, False, False)
    GRAY_SHULKER_BOX = \
        Block(226, 0, "minecraft:gray_shulker_box", "Gray Shulker Box", True, 0, False, False)
    SILVER_SHULKER_BOX = \
        Block(227, 0, "minecraft:silver_shulker_box", "Light Gray Shulker Box", True, 0, False, False)
    CYAN_SHULKER_BOX = \
        Block(228, 0, "minecraft:cyan_shulker_box", "Cyan Shulker Box", True, 0, False, False)
    PURPLE_SHULKER_BOX = \
        Block(229, 0, "minecraft:purple_shulker_box", "Purple Shulker Box", True, 0, False, False)
    BLUE_SHULKER_BOX = \
        Block(230, 0, "minecraft:blue_shulker_box", "Blue Shulker Box", True, 0, False, False)
    BROWN_SHULKER_BOX = \
        Block(231, 0, "minecraft:brown_shulker_box", "Brown Shulker Box", True, 0, False, False)
    GREEN_SHULKER_BOX = \
        Block(232, 0, "minecraft:green_shulker_box", "Green Shulker Box", True, 0, False, False)
    RED_SHULKER_BOX = \
        Block(233, 0, "minecraft:red_shulker_box", "Red Shulker Box", True, 0, False, False)
    BLACK_SHULKER_BOX = \
        Block(234, 0, "minecraft:black_shulker_box", "Black Shulker Box", True, 0, False, False)
    WHITE_GLAZED_TERRACOTTA = \
        Block(235, 0, "minecraft:white_glazed_terracotta", "White Glazed Terracotta", True, 0, False, False)
    ORANGE_GLAZED_TERRACOTTA = \
        Block(236, 0, "minecraft:orange_glazed_terracotta", "Orange Glazed Terracotta", True, 0, False, False)
    MAGENTA_GLAZED_TERRACOTTA = \
        Block(237, 0, "minecraft:magenta_glazed_terracotta", "Magenta Glazed Terracotta", True, 0, False, False)
    LIGHT_BLUE_GLAZED_TERRACOTTA = \
        Block(238, 0, "minecraft:light_blue_glazed_terracotta", "Light Blue Glazed Terracotta", True, 0, False, False)
    YELLOW_GLAZED_TERRACOTTA = \
        Block(239, 0, "minecraft:yellow_glazed_terracotta", "Yellow Glazed Terracotta", True, 0, False, False)
    LIME_GLAZED_TERRACOTTA = \
        Block(240, 0, "minecraft:lime_glazed_terracotta", "Lime Glazed Terracotta", True, 0, False, False)
    PINK_GLAZED_TERRACOTTA = \
        Block(241, 0, "minecraft:pink_glazed_terracotta", "Pink Glazed Terracotta", True, 0, False, False)
    GRAY_GLAZED_TERRACOTTA = \
        Block(242, 0, "minecraft:gray_glazed_terracotta", "Gray Glazed Terracotta", True, 0, False, False)
    LIGHT_GRAY_GLAZED_TERRACOTTA = \
        Block(243, 0, "minecraft:light_gray_glazed_terracotta", "Light Gray Glazed Terracotta", True, 0, False, False)
    CYAN_GLAZED_TERRACOTTA = \
        Block(244, 0, "minecraft:cyan_glazed_terracotta", "Cyan Glazed Terracotta", True, 0, False, False)
    PURPLE_GLAZED_TERRACOTTA = \
        Block(245, 0, "minecraft:purple_glazed_terracotta", "Purple Glazed Terracotta", True, 0, False, False)
    BLUE_GLAZED_TERRACOTTA = \
        Block(246, 0, "minecraft:blue_glazed_terracotta", "Blue Glazed Terracotta", True, 0, False, False)
    BROWN_GLAZED_TERRACOTTA = \
        Block(247, 0, "minecraft:brown_glazed_terracotta", "Brown Glazed Terracotta", True, 0, False, False)
    GREEN_GLAZED_TERRACOTTA = \
        Block(248, 0, "minecraft:green_glazed_terracotta", "Green Glazed Terracotta", True, 0, False, False)
    RED_GLAZED_TERRACOTTA = \
        Block(249, 0, "minecraft:red_glazed_terracotta", "Red Glazed Terracotta", True, 0, False, False)
    BLACK_GLAZED_TERRACOTTA = \
        Block(250, 0, "minecraft:black_glazed_terracotta", "Black Glazed Terracotta", True, 0, False, False)
    CONCRETE = \
        Block(251, 0, "minecraft:concrete", "White Concrete", True, 0, False, False)
    CONCRETE_1 = \
        Block(251, 1, "minecraft:concrete_1", "Orange Concrete", True, 0, False, False)
    CONCRETE_2 = \
        Block(251, 2, "minecraft:concrete_2", "Magenta Concrete", True, 0, False, False)
    CONCRETE_3 = \
        Block(251, 3, "minecraft:concrete_3", "Light Blue Concrete", True, 0, False, False)
    CONCRETE_4 = \
        Block(251, 4, "minecraft:concrete_4", "Yellow Concrete", True, 0, False, False)
    CONCRETE_5 = \
        Block(251, 5, "minecraft:concrete_5", "Lime Concrete", True, 0, False, False)
    CONCRETE_6 = \
        Block(251, 6, "minecraft:concrete_6", "Pink Concrete", True, 0, False, False)
    CONCRETE_7 = \
        Block(251, 7, "minecraft:concrete_7", "Gray Concrete", True, 0, False, False)
    CONCRETE_8 = \
        Block(251, 8, "minecraft:concrete_8", "Light Gray Concrete", True, 0, False, False)
    CONCRETE_9 = \
        Block(251, 9, "minecraft:concrete_9", "Cyan Concrete", True, 0, False, False)
    CONCRETE_10 = \
        Block(251, 10, "minecraft:concrete_10", "Purple Concrete", True, 0, False, False)
    CONCRETE_11 = \
        Block(251, 11, "minecraft:concrete_11", "Blue Concrete", True, 0, False, False)
    CONCRETE_12 = \
        Block(251, 12, "minecraft:concrete_12", "Brown Concrete", True, 0, False, False)
    CONCRETE_13 = \
        Block(251, 13, "minecraft:concrete_13", "Green Concrete", True, 0, False, False)
    CONCRETE_14 = \
        Block(251, 14, "minecraft:concrete_14", "Red Concrete", True, 0, False, False)
    CONCRETE_15 = \
        Block(251, 15, "minecraft:concrete_15", "Black Concrete", True, 0, False, False)
    CONCRETE_POWDER = \
        Block(252, 0, "minecraft:concrete_powder", "White Concrete Powder", True, 0, False, False)
    CONCRETE_POWDER_1 = \
        Block(252, 1, "minecraft:concrete_powder_1", "Orange Concrete Powder", True, 0, False, False)
    CONCRETE_POWDER_2 = \
        Block(252, 2, "minecraft:concrete_powder_2", "Magenta Concrete Powder", True, 0, False, False)
    CONCRETE_POWDER_3 = \
        Block(252, 3, "minecraft:concrete_powder_3", "Light Blue Concrete Powder", True, 0, False, False)
    CONCRETE_POWDER_4 = \
        Block(252, 4, "minecraft:concrete_powder_4", "Yellow Concrete Powder", True, 0, False, False)
    CONCRETE_POWDER_5 = \
        Block(252, 5, "minecraft:concrete_powder_5", "Lime Concrete Powder", True, 0, False, False)
    CONCRETE_POWDER_6 = \
        Block(252, 6, "minecraft:concrete_powder_6", "Pink Concrete Powder", True, 0, False, False)
    CONCRETE_POWDER_7 = \
        Block(252, 7, "minecraft:concrete_powder_7", "Gray Concrete Powder", True, 0, False, False)
    CONCRETE_POWDER_8 = \
        Block(252, 8, "minecraft:concrete_powder_8", "Light Gray Concrete Powder", True, 0, False, False)
    CONCRETE_POWDER_9 = \
        Block(252, 9, "minecraft:concrete_powder_9", "Cyan Concrete Powder", True, 0, False, False)
    CONCRETE_POWDER_10 = \
        Block(252, 10, "minecraft:concrete_powder_10", "Purple Concrete Powder", True, 0, False, False)
    CONCRETE_POWDER_11 = \
        Block(252, 11, "minecraft:concrete_powder_11", "Blue Concrete Powder", True, 0, False, False)
    CONCRETE_POWDER_12 = \
        Block(252, 12, "minecraft:concrete_powder_12", "Brown Concrete Powder", True, 0, False, False)
    CONCRETE_POWDER_13 = \
        Block(252, 13, "minecraft:concrete_powder_13", "Green Concrete Powder", True, 0, False, False)
    CONCRETE_POWDER_14 = \
        Block(252, 14, "minecraft:concrete_powder_14", "Red Concrete Powder", True, 0, False, False)
    CONCRETE_POWDER_15 = \
        Block(252, 15, "minecraft:concrete_powder_15", "Black Concrete Powder", True, 0, False, False)
    STRUCTURE_BLOCK = \
        Block(255, 0, "minecraft:structure_block", "Structure Block", True, 0, False, False)
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
           "255": STRUCTURE_BLOCK}


Blocks = _Blocks()
