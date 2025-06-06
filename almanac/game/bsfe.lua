local almanac = require("almanac")
local workspaces = almanac.workspaces

local util = almanac.util

local fe2 = require("almanac.game.fe2")


local Character = {}
local Job = {}
local Item = {}
---------------------------------------------------
-- Inventory --
---------------------------------------------------
local inventory = fe2.Character.inventory:use_as_base()
inventory.eff_multiplier = 3
inventory.eff_might = false
inventory:get_calc("atk").func = function(data, unit, item)
if item:is_magic() then
    return item.stats.mt
else
    return unit.stats.atk + item.stats.mt
end end
---------------------------------------------------
-- Character --
---------------------------------------------------
Character.__index = Character
setmetatable(Character, workspaces.Character)

Character.section = almanac.get("database/bsfe/char.json")
Character.helper_job_growth = false
Character.helper_portrait = "database/bsfe/images"

Character.compare_cap = false

Character.inventory = inventory

Character.Job = Job
Character.Item = Item

function Character:setup()
    self.job = self.Job:new(self.options.class)
    
end

function Character:default_options()
    return {
        class = self.data.job
    }
end

function Character:show_cap()
    return nil
end

function Character:get_cap()
    return {hp = 52, atk = 40, skl = 40, spd = 40, lck = 40, def = 40, res = 40}
end

function Character:final_base()
    
    local base = self:calc_base()

    -- For reclass games
    if not self.average_classic then
        if self.helper_job_base and not self:is_personal() then         
            base = util.math.add_stats(base, self.job:get_base())
            base.hp = base.hp - self.job.data.base.hp
            base.hp = base.hp + math.max(self.job.data.base.hp, self.data.base.hp)

            base.wlv = base.wlv - self.job.data.base.wlv 
            base.wlv = base.wlv + math.max(self.job.data.base.wlv, self.data.base.wlv )
        
          --[[
            print(self.job.data.name)
            if self.promo_remove_hp then
                base.hp = base.hp - self.job:get_base().hp
            end
            print('reclass')
            print(base.hp)
            ]]
        end
    
    -- Non reclass games
    else
        -- Apply base class stats
        local job = self.data.job
        if self:is_changed("class") then 
            job = self.job 
        else 
            job = self.Job:new(self.data.job) 
        end

        print(job.data.name)
        
        base = base + job:get_base()
        
        if self:has_averages() then
            base = self:calc_averages_classic(base)
        end
        
        if self.personal then
            base = base - job:get_base()
        end
    end
    
    base = self:common_base(base)
    
    return base
end

function Character:calc_averages(base, args)
    args = args or {}

    local calculator = self.avg:set_character(self)

    for k, v in pairs(args) do
        calculator[k] = v
    end

    base = calculator:calculate(base, self:get_lvl(), self.lvl, self.job_averages)
    return base
end

function Character:calc_base()
    local base = self:get_base()
    local job = self.Job:new(self.data.job)


    if not self.average_classic and self:has_averages() then
        base = self:calc_averages(base)
    end
   

    return base
end



function Character:get_rank_bonus(job1, job2)
    text = ""
    return text
end

function Character:show_rank()
    return self.job:show_rank()
end


function Character:get_promo_bonus(job1, job2)
    local promo
    promo = util.math.sub_stats(job2:get_base(), job1:get_base())
    promo['hp'] = 0
    promo = util.math.remove_zero(promo)
    return promo
end

---------------------------------------------------
-- Item --
---------------------------------------------------
Item.__index = Item
setmetatable(Item, fe2.Item)

Item.section = almanac.get("database/bsfe/item.json")



--------------------------------------------------
-- Job --
---------------------------------------------------
Job.__index = Job
setmetatable(Job, almanac.workspaces.Job)
Job.section = almanac.get("database/bsfe/job.json")
Job.hp_bonus = false

function Job:can_dismount()
    return self.data.dismount
end

function Job:show_dismount()
    return "**Dismount**: " .. 
    util.table_stats(self:get_dismount(), {value_start = "+"})
end

function Job:get_dismount()
    local dismount = Job:new(self.data.dismount)
    local stats = util.math.sub_stats(dismount:get_base(), self:get_base(), {})  
    stats['wlv'] = 0 
    stats['hp'] = 0 
    stats = util.math.remove_zero(stats)
    return stats
end

function Job:show_rank()
    return util.text.weapon_no_rank(self.data.weapon)
end

return {
    Character = Character,
    Job = Job,
    Item = Item,
}
