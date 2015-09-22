import random;                      
#Pathfinder weapons generator v. 0.1
#Credit where credit's due, this is highly inspired by PhatLoots.
#Wait, wasn't that the chest one?
#OK then, Borderlands.
#License: MIT License
#Changelog: Removed random elemental chance for now. Instead, letting it choose between ALL the weapon types instead of just the lame stuff.
#Roadmap: Add a chance for the weapon to be CAAAAAARSED and add back special effect chances. (The framework is done with 0.2, now add coolness)
################################################################################
battleAspergilium='Battle Aspergiluim: 5 gp 1 d4 1d6 x2 4 lb. B Holy Water';
brassKnife='Brass Knife: 2gp 1d3 1d4 19-20/x2 10 ft  lb P or S fragile';
brassKnuckles='Brass Knuckles: 1 gp 1d2 1d3 2 —  1 lb. B monk';
cestus='Cestus: 5 gp 1d3 1d4 19-20/×2 — 1 lb. B or P monk';
dagger='Dagger: 2 gp 1d3 1d4 19-20/×2 10 ft. 1 lb. P or S —';
punchingDagger='Punching Dagger: 2 gp 1d3 1d4 x3 — 1 lb. P —';
spikedGauntlet='Spiked Gauntlet: 5 gp 1d3 1d4 ×2 — 1 lb. P —';
hookHand='Hook fer a Hand: 10 gp 1d3 1d4 ×2 — 1 lb. S';
kunai='Kunai: 2 gp 1d3 1d4 ×2 10 ft. 2 lbs. B or P —';
lightMace='Light Mace: 5 gp 1d4 1d6 ×2 — 4 lbs. B —';
sickle='Sickle: 6 gp 1d4 1d6 ×2 — 2 lbs. S trip';
woodenStake='Wooden Stake: — 1d3 1d4 ×2 10 ft. 1 lb. P —';
#Variables containing the names and properties of the various light weapons
lightMeleeWeapons=[battleAspergilium,brassKnife,brassKnuckles,cestus,punchingDagger,spikedGauntlet,hookHand,kunai,lightMace,sickle,woodenStake];
#Simple list containing all the light melee weapons and their info
lightMeleeNames=['Quick','Light','Small','Cunning','Clever','Mildly Lethal','Mostly Harmless'];
#List of random adjectives to put in front of the light weapons to provide them with a somewhat in-context Name
################################################################################
club='Club — 1d4 1d6 ×2 10 ft. 3 lbs. B —';
mereClub='Mere Club 2 gp 1d3 1d4 ×2 — 2 lbs. B or P fragile';
heavyMace='Heavy Macev12 gp 1d6 1d8 ×2 — 8 lbs. B —';
morningstar='Morningstar 8 gp 1d6 1d8 ×2 — 6 lbs. B and P —';
shortspear='Shortspear 1 gp 1d4 1d6 ×2 20 ft. 3 lbs. P —';
#All the one-handed melee weapons
oneHandedMeleeWeapons=[club,mereClub,heavyMace,morningstar,shortspear];
#Combining said variables into a nice, manageable list o' weapons
oneHandedMeleeNames=['Substantial','Heavy','Hefty','Authoritative','Battle-Hardened'];
################################################################################
bayonet='Bayonet 5 gp 1d4 1d6 ×2 — 1 lb. P —';
boardingPike='Boarding Pike 8 gp 1d6 1d8 x3 — 9 lbs. P brace, reach';
kumade='Kumade 5 gp 1d4 1d6 ×3 — 4 lbs. P grapple';
collapsibleKumade='Kumade, collapsible 10 gp 1d4 1d6 ×3 — 4 lbs. P grapple';
longspear='Longspear 5 gp 1d6 1d8 x3 — 9 lbs. P brace, reach';
quarterstaff='Quarterstaff — 1d4/1d4 1d6/1d6 ×2 — 4 lbs. B double, monk';
spear='Spear 2 gp 1d6 1d8 x3 20 ft. 6 lbs. P brace';
boarSpear='Boar spear 5 gp 1d6 1d8 ×2 — 8 lb. P brace, see text';
weightedSpear='Weighted spear 10 gp 1d6/1d4 1d8/1d6 ×3/×2 — 8 lbs. B or P brace, double';
twoFistedMeleeWeapons=[bayonet,boardingPike,kumade,collapsibleKumade,longspear,quarterstaff,boarSpear,weightedSpear];
twoFistedMeleeNames=['Lengthy','Ten-Foot','Pointy','Oak','Birch','Pine','Reliable','Simple'];
################################################################################
blowgun='Blowgun 2 gp 1 1d2 ×2 20 ft. 1 lb. P —';
heavyCrossbow='Heavy crossbow 50 gp 1d8 1d10 19-20/×2 120 ft. 8 lbs. P —';
heavyCrossbowUnderwater='Heavy crossbow (underwater) 100 gp 1d8 1d10 19-20/×2 120 ft. 8 lbs. P —';
lightCrossbow='Light crossbow 35 gp 1d6 1d8 19-20/×2 80 ft. 4 lbs. P —';
lightCrossbowUnderwater='Light crossbow (underwater) 70 gp 1d6 1d8 19-20/×2 80 ft. 4 lbs. P —';
dart='Dart 5 sp 1d3 1d4 ×2 20 ft. 1/2 lb. P —';
javelin='Javelin 1 gp 1d4 1d6 ×2 30 ft. 2 lbs. P —';
sling='Sling — 1d3 1d4 ×2 50 ft. — B —';
stingChuck='Stingchuck — 1d3 1d4 ×2 10 ft. 9 lbs. B see text';
stonebow='Stonebow 35 gp 1d4 1d6 ×2 50 ft. 4 lbs. B —';
rangedWeapons=[blowgun,heavyCrossbow,heavyCrossbowUnderwater,lightCrossbow,lightCrossbowUnderwater,dart,javelin,sling,stingChuck,stonebow];
rangedNames=['Hawkeye','Bullseye','Far-Flying','True-Shot','Jakobs','Hyperion'];
################################################################################
boardingAxe='Boarding axe 6 gp 1d4 1d6 x3 — 3 lbs. P or S —';
throwingAxe='Throwing axe 8 gp 1d4 1d6 ×2 10 ft. 2 lbs. S —';
bladeBoot='Blade boot 25 gp 1d3 1d4 ×2 — 2 lbs. P see text';
ninetails='Cat-of-nine-tails 1 gp 1d3 1d4 ×2 — 1 lb. S disarm, nonlethal';
dogslicer='Dogslicer 8 gp 1d4 1d6 19-20/×2 — 1 lb. S fragile';
lightHammer='Light hammer 1 gp 1d3 1d4 ×2 20 ft. 2 lbs. B —';
gladius='Gladius 15 gp 1d4 1d6 19-20/×2 — 3 lbs. P or S performance';
handaxe='Handaxe 6 gp 1d4 1d6 x3 — 3 lbs. S —';
switchblade='Switchblade 5 gp 1d3 1d4 19-20/×2 10 ft. 1 lb. P —';
kukri='Kukri 8 gp 1d3 1d4 18–20/x2 — 2 lbs. S —';
machete='Machete 10 gp 1d4 1d6 19-20/×2 — 2 lbs. S —';
lightPick='Light pick 4 gp 1d3 1d4 x4 — 3 lbs. P —';
ratfolkTailblade='Ratfolk tailblade 11 gp 1d2 1d3 20/×2 — 1/2 lb. S —';
sap='Sap 1 gp 1d4 1d6 ×2 — 2 lbs. B nonlethal';
seaKnife='Sea-knife 8 gp 1d3 1d4 19-20/×2 — 1 lb. S —';
starKnife='Starknife 24 gp 1d3 1d4 x3 20 ft. 3 lbs. P —';
shortSword='Shortsword10 gp 1d4 1d6 19-20/×2 — 2 lbs. P —';
warRazor='War razor 8 gp 1d3 1d4 19-20/×2 — 1 lb. S —';
lightMartialWeapons=[boardingAxe,throwingAxe,bladeBoot,ninetails,dogslicer,lightHammer,gladius,handaxe,switchblade,kukri,machete,lightPick,ratfolkTailblade,sap,seaKnife,starKnife,shortSword,warRazor];
lightMartialNames=['Scourging','Scathing','Blistering','Gore-Spattered','Eviscerating','Brutal'];
########Lots o' exceptions with the martial light melees.(kobold,armor)#########
ankus='Ankus 8 gp 1d6 1d8 ×2 — 5 lbs. P disarm, trip';
battleaxe='Battleaxe 10 gp 1d6 1d8 x3 — 6 lbs. S —';
combatScabbard='Combat scabbard  1 gp  1d4 1d6 x2   —  1 lb.  B improvised, see text';
cutlass='Cutlass 15 gp 1d4 1d6 18-20/×2 — 4 lbs. S —';
flail='Flail 8 gp 1d6 1d8 ×2 — 5 lbs. B disarm, trip';
gandasa='Gandasa 15 gp 1d6 2d4 ×3 — 4 lbs. S —';
klar='Klar 12 gp 1d4 1d6 ×2 — 6 lbs. S —';
longsword='Longsword 15 gp 1d6 1d8 19-20/×2 — 4 lbs. S —';
manople='Manople 17 gp 1d6 1d8 ×2 — 4 lbs. P or S blocking, disarm';
heavyPick='Heavy pick 8 gp 1d4 1d6 x4 — 6 lbs. P —';
rapier='Rapier 20 gp 1d4 1d6 18–20/×2 — 2 lbs. P —';
combatScabbardSharp='Combat scabbard (sharpened) 10 gp 1d4 1d6 ×2 — 1 lb. S see text';
scimitar='Scimitar 15 gp 1d4 1d6 18–20/×2 — 4 lbs. S —';
scizore='Scizore 20 gp 1d8 1d10 ×2 — 3 lbs. P —';
swordCane='Sword cane 45 gp 1d4 1d6 ×2 — 4 lbs. P see text';
terbutje='Terbutje 5 gp 1d6 1d8 19-20/×2 — 2 lbs. S fragile';
steelTerbutje='Steel terbutje 20 gp 1d6 1d8 19-20/×2 — 4 lbs. S —';
trident='Trident 15 gp 1d6 1d8 ×2 10 ft. 4 lbs. P brace';
warhammer='Warhammer 12 gp 1d6 1d8 x3 — 5 lbs. B —';
oneHandedMartialWeapons=[ankus,battleaxe,combatScabbard,cutlass,flail,gandasa,klar,longsword,manople,heavyPick,rapier,combatScabbardSharp,scimitar,scizore,swordCane,terbutje,steelTerbutje,warhammer];
oneHandedMartialNames=['Blood-Drenched','War-Weary','Fantastic','Elusive','Dominating','Kingdombreaker','Murdering','Lethal','Aetheric','Well-Balanced'];
###################Couple more shield 'n armor exceptions.######################
d6=(1,2,3,4,5,6);
d20=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20);
rolld6=random.choice(d6);
if rolld6==1:
    outputStr=[random.choice(lightMeleeNames),random.choice(lightMeleeWeapons)];
#Pairs a random light weapon name with a random light weapon type
if rolld6==2:
    outputStr=[random.choice(oneHandedMeleeNames),random.choice(oneHandedMeleeWeapons)];
if rolld6==3:
    outputStr=[random.choice(twoFistedMeleeNames),random.choice(twoFistedMeleeWeapons)];
if rolld6==4:
    outputStr=[random.choice(rangedNames),random.choice(rangedWeapons)];
if rolld6==5:
    outputStr=[random.choice(lightMartialNames),random.choice(lightMartialWeapons)];
if rolld6==6:
    outputStr=[random.choice(oneHandedMartialNames),random.choice(oneHandedMartialWeapons)];
elementalDamage=['Electric Elemental','Water Elemental','Fire Elemental','Air Elemental'];

rolld20=random.choice(d20);
if rolld20==1:
    print('-1 CAAAAAAAAAAAAAAARSED');
if rolld20==20:
    print('+1');
rollagaind6=random.choice(d6);
if rollagaind6==6:
    print(random.choice(elementalDamage));
    
#1-in-20 chance that the weapon will be caaaarsed.
print (outputStr)
#Here's your weapon!

                      

