import json
import copy

def refine_equip(key, rng, eff):
    stats = ["atk", "spd", "def", "res"]
    if (eff):
        stats.append("eff")

    ranged = True
    if int(rng) == 1:
        ranged = False

    # load the original weapon as obj
    with open('../database/feh/equip.json', 'r') as f:
        weapons = json.load(f)
    obj = weapons[key]

    for j in stats:
        # create a separate copy of the original to modify w/ refine
        refine = copy.deepcopy(obj)
        refine['name'] = weapons[key]['refine'] + ' (+' + j.capitalize() + ')'
        refine['refine'] = False
        d = refine['bonus']
        if j == 'atk':
            if ranged:
                d[j] = d.get(j, 0) + 1
                refine['bonus']['hp'] = 2
            else:
                d[j] = d.get(j, 0) + 2
                refine['bonus']['hp'] = 5
        elif j == 'spd':
            if ranged:
                d[j] = d.get(j, 0) + 2
                refine['bonus']['hp'] = 2
            else:
                d[j] = d.get(j, 0) + 3
                refine['bonus']['hp'] = 5
        elif j == 'def':
            if ranged:
                d[j] = d.get(j, 0) + 3
                refine['bonus']['hp'] = 2
            else:
                d[j] = d.get(j, 0) + 4
                refine['bonus']['hp'] = 5
        elif j == 'res':
            if ranged:
                d[j] = d.get(j, 0) + 3
                refine['bonus']['hp'] = 2
            else:
                d[j] = d.get(j, 0) + 4
                refine['bonus']['hp'] = 5
        elif j == 'eff':
            if not ranged:
                refine['bonus']['hp'] = 3

        index = key + j
        weapons[index] = refine

        with open('../database/feh/equip.json', 'w') as fp:
            json.dump(weapons, fp, indent=2)

    return


def new_equip(key):
    with open('../database/feh/skill.json', 'r') as f:
        skill = json.load(f)

    weapon = skill[key]
    eff = False

    equip = {}

    equip['name'] = weapon['name']
    equip['bonus'] = {}
    equip['refine'] = False
    if '+' in equip['name'] or 'Arcane' in equip['name'] or 'Arc.' in equip['name']: 
        equip['name'] = equip['name'] + ' (Unrefined)'
        equip['refine'] = weapon['name']
    if weapon['refine']:
        equip['name'] = equip['name'] + ' (Unrefined)'
        equip['refine'] = weapon['name']
        eff = True

    equip['bonus']['atk'] = int(weapon['skill'][0]['stats']['mt'])

    # Try to find stat boosts

    desc = weapon['skill'][0]['description']
    desc = desc.split('.')
    for j in desc:
        if (j.startswith("Grants") or j.startswith(" Grants")):
            pieces = j.split(' ')
            pieces = [i for i in pieces if i]
            if len(pieces) > 2:
                continue
            pieces.pop(0)

            arr = pieces[0].split('+')
            stats = arr[0].lower()
            if ('/' in stats):
                stats = stats.split('/')
            boost = int(arr[1])

            if stats is not list:
                if stats == 'atk':
                    equip['bonus']['atk'] = equip['bonus']['atk'] + boost
                else:
                    equip['bonus'][stats] = boost

            else:
                for i in stats:
                    if i == 'atk':
                        equip['bonus']['atk'] = equip['bonus']['atk'] + boost
                    else:
                        equip['bonus'][i] = boost

    with open('../database/feh/equip.json', 'r', encoding="utf-8") as f:
        equips = json.load(f)

    equips[key] = equip

    with open('../database/feh/equip.json', 'w') as fp:
        json.dump(equips, fp, indent=2)

    if (equip['refine']):
        obj = refine_equip(key, weapon['skill'][0]['stats']['rng'], eff)


weps = [
    'lucrativebow',
    'perspicacious',
    'foragernaginata',
    'raudrlantern',
    'tripathsplitter',
    'heavywaraxe',
    'exaltswarstaff',
    'newwaraxe',
    'fellwartome',
    'draconicpacts',
    'emblemragnell',
    'vulturebow',
    'lightbursttome',
    'tenderexcalibur',
    'sunlight',
    'purewingspear',
    'luckybow',
    'daydreamegg',
    'flingsterspear',
    'skyhopperegg',
    'hippityhopaxe',
    'carrotbow',
    'luckybow',
    'divineonesarts',
    'penitentlance',
    'arcanecharmer',
    'iceboundtome',
    'axeofadoration',
    'reversalblade',
    'devotedbasket',
    'axeofdevotion',
    'tendervessel',
    'lovingbreath',
    'righteouslance',
    'airbornespear',
    'herokingsword',
    'monarchsstone',
    'nabatalance',
    'bladeofsands',
    'nabatabeacon',
    'arcadianaxes',
    'sandglassbow',
    'stoutheartlance',
    'bladeroyale',
    'repair',
    'thief',
    'cleverdagger',
    'arcanethunder',

    'hadeso',
    'darkscripture',
    'danielmadebow',
    'astralbreath',
    'bridesfang',
    'aurorabreath',
    'brutalbreath',
    'skinfaxi',
    'crusher',
    'joyfulvows',
    'levindagger',
    'lyngheidr',
    'feathersword',
    'gurgurant',
    'rinkahsclub',
    'flowerofsorrow',
    'persecutionbow',
    'studiedforblaze',
    'miragerod',
    'dragoonaxe',
    'windsofchange',
    'constantdagger',
    'primordialbreath',



]

for i in weps:
    new_equip(i)
