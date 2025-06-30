local almanac = require("almanac")

local util = almanac.util

local Infobox = almanac.Infobox
local Pagebox = almanac.Pagebox

local fe15 = require("almanac.game.fe15")

local Character = {}
local Job = {}
local Item = {}

---------------------------------------------------
-- Inventory --
---------------------------------------------------
local inventory = fe15.Character.inventory:use_as_base()
inventory.eff_multiplier = 3
inventory.eff_might = false
inventory:get_calc("hit").func = function(data, unit, item)
if item:is_magic() then
    return item.stats.hit
else
    return item.stats.hit + unit.stats.skl
end end

---------------------------------------------------
-- Character --
---------------------------------------------------
Character.__index = Character
setmetatable(Character, fe15.Character)

Character.section = almanac.get("database/fe2/char.json")
Character.helper_portrait = "database/fe2/images"

Character.helper_job_growth = false

Character.compare_cap = false

Character.inventory = inventory

Character.Job = Job
Character.Item = Item

function Character:default_options()
    return {
        class = self.data.job
    }
end

function Character:setup()
    self.job = self.Job:new(self.options.class)
end

-- Mod
function Character:show_info()
    local infobox = self:show_mod()
    
    if self.job:can_promo() then
        local promo = self.job:get_promo()
        
        promo_text = promo:promo_bonus(self:final_base())
        promo_text = util.table_stats(promo_text)
        
        local name = promo:get_name()
        
        if self.job.data.lvl then
            name = string.format("%s (Lv. %s)", name, self.job.data.lvl)
        end
        
        infobox:insert(name, "(Raise to these stats if they are lower)\n" .. promo_text, true)
    end
    
    infobox:image("thumbnail", self:get_portrait())
    
    -- Return page infobox if it has magic
    if self.data.black or self.data.white then
        local magicbox = Infobox:new({title = self:get_name()})
        
        if self.data.black then
            magicbox:insert("Mage", self:show_magic(self.data.black), true)
        end
        
        if self.data.white then
            magicbox:insert("Cleric", self:show_magic(self.data.white), true)
        end
        
        local pagebox = Pagebox:new()
        
        pagebox:stats_button()
        pagebox:button({page = 1, label = "Spell", emoji = "magic"})
        
        pagebox:page(infobox)
        pagebox:page(magicbox)
        
        return pagebox
        
    else
        return infobox
    end
    
end

function Character:show_magic(data)
    local text = ""
    
    for key, value in pairs(data) do
        local item = self.Item:new(key)
        
        local line = string.format("Lv. %s %s", value.lvl, item:get_name())
        
        if value.promo then
            line = util.text.bold(line)
        end
        
        text = text .. line .. "\n"
    end
    
    return text
end

function Character:get_mod()
    local text = self:get_lvl_mod()
    
    text = text .. self:common_mods()
    
    return text
end

-- Base
function Character:final_base()
    local base = self:calc_base()
    
    if self.job.id ~= self.data.job then
        local promo = self.job:promo_bonus(base)
        
        base = util.math.rise_stats(base, promo)
    
    else
        -- Add move from base class
        base = util.math.add_stats(base, self.job:get_base(), {ignore_existing = true})
    end

    -- if its dreadfighter
    if self.job.id == "dreadfighter" then
        local res = 15

        base.res = math.max(res + base.res, 0)
    end

    base = self:common_base(base)
    
    return base
end

-- Growth
function Character:calc_growth()
    local growth = self:get_growth()
    
    if self.shards then
        for i, shard in ipairs(self.shards) do
            growth = growth + shard_bonus[shard]
        end
    end
    
    return growth
end

-- Ranks
function Character:show_rank()
    return self.job:show_rank()
end

function Character:show_cap()
    return nil
end

function Character:get_cap()
    return {hp = 52, atk = 40, skl = 40, spd = 40, lck = 40, def = 40, res = 40}
end

---------------------------------------------------
-- Job --
---------------------------------------------------
Job.__index = Job
setmetatable(Job, fe15.Job)

Job.section = almanac.get("database/fe2/job.json")
Job.hp_bonus = false


function Job:show()
    local infobox = fe15.Job.show(self)
    
    -- Change the bases to display the res
    infobox.fields[1].value = util.table_stats(self:get_base(true))
    
    return infobox
end

function Job:promo_bonus(base)
    
    local job = self:get_base()
    
    local promo = util.math.rise_stats(base, job, {
    ignore = {"res", "mov", "lck"}, check = bonus_check, ignore_unchanged = true})
    
    -- mov always is fixed
    promo.mov = job.mov

    return promo
end

function Job:show_rank()
    return util.text.weapon_no_rank(self.data.weapon, {pack = pack})
end

-- Only return the res for display stuff
function Job:get_base(display)
    local base = util.copy(self.data.base)
    
    if not display then
        base.res = 0
    end
    
    return base
end

---------------------------------------------------
-- Item --
---------------------------------------------------
Item.__index = Item
setmetatable(Item, fe15.Item)

Item.section = almanac.get("database/fe2/item.json")

return {
    Character = Character,
    Job = Job,
    Item = Item
}