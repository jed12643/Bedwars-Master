 local kavoUi = loadstring(game:HttpGet("https://pastebin.com/raw/vff1bQ9F"))()
local window = kavoUi.CreateLib("Bedwars | Master","DarkTheme")

---Tabs

local Tab1 = window:NewTab("Combat")
local Tab1Section = Tab1:NewSection("Nuker")
local Tab1Section = Tab1:NewSection("KillAura")
local Tab1Section = Tab1:NewSection("No Fall Damage")
local Tab1Section = Tab1:NewSection("Walkspeed")
local Tab1Section = Tab1:NewSection("Jumppower")
local Tab2 = window:NewTab("Player")
local Tab2Section = Tab2:NewSection("Inf Jumps")
local Tab2Section = Tab2:NewSection("Autosprint")
local Tab2Section = Tab2:NewSection("NoSlowdown")
local Tab2Section = Tab2:NewSection("Fly-Bypass")
local Tab3 = window:NewTab("Animations")
local Tab3Section = Tab3:NewSection("Zombie")
local Tab3Section = Tab3:NewSection("Astronaut")
local Tab3Section = Tab3:NewSection("Bubbly")
local Tab3Section = Tab3:NewSection("Cartoony")
local Tab3Section = Tab3:NewSection("Elder")
local Tab3Section = Tab3:NewSection("Night")
local Tab3Section = Tab3:NewSection("Elder")
local Tab3Section = Tab3:NewSection("Superhero")
local Tab3Section = Tab3:NewSection("Toy")
local Tab3Section = Tab3:NewSection("Mage")
local Tab3Section = Tab3:NewSection("Levitation")
local Tab3Section = Tab3:NewSection("Robot")
local Tab3Section = Tab3:NewSection("Ninja")
local Tab3Section = Tab3:NewSection("Vampire")
local Tab3Section = Tab3:NewSection("Werewolf")
local Tab3Section = Tab3:NewSection("Stylish")
local Tab3Section = Tab3:NewSection("Pirate")
local Tab3Section = Tab3:NewSection("Oldschool")
local Tab4 = window:NewTab("Credits")
local Tab4Section = Tab4:NewSection("Made By SubTobacon")
local Tab4Section = Tab4:NewSection("Oditor By SubTo_bacon")
local Tab4Section = Tab4:NewSection("Others Name")
local Tab5 = window:NewTab("All Hubs")
local Tab5Section = Tab5:NewSection("Inf Yield")
local Tab5Section = Tab5:NewSection("Keyboard")

---Buttons

Tab1Section:NewButton("Hitbox","Increase Range",function()
_G.HeadSize = 25
_G.Disabled = true

game:GetService('RunService').RenderStepped:connect(function()
if _G.Disabled then
for i,v in next, game:GetService('Players'):GetPlayers() do
if v.Name ~= game:GetService('Players').LocalPlayer.Name then
pcall(function()
v.Character.HumanoidRootPart.Size = Vector3.new(_G.HeadSize,_G.HeadSize,_G.HeadSize)
v.Character.HumanoidRootPart.Transparency = 0.7
v.Character.HumanoidRootPart.BrickColor = BrickColor.new("Really black")
v.Character.HumanoidRootPart.Material = "Neon"
v.Character.HumanoidRootPart.CanCollide = false
end)
end
end
end
end)
end)

Tab1Section:NewButton("Invisible","Makes You Invisible",function()
-- FE Invisible

Local = game:GetService('Players').LocalPlayer
Char  = Local.Character
touched,tpdback = false, false
Local.CharacterAdded:connect(function(char)
    if script.Disabled ~= true then
        wait(.25)
        loc = Char.HumanoidRootPart.Position
        Char:MoveTo(box.Position + Vector3.new(0,.5,0))
    end
end)
game:GetService('UserInputService').InputBegan:connect(function(key)
    if key.KeyCode == Enum.KeyCode.Equals then
        if script.Disabled ~= true then
            script.Disabled = true
            print'you may re-execute'
        end
    end
end)
box = Instance.new('Part',workspace)
box.Anchored = true
box.CanCollide = true
box.Size = Vector3.new(10,1,10)
box.Position = Vector3.new(0,10000,0)
box.Touched:connect(function(part)
    if (part.Parent.Name == Local.Name) then
        if touched == false then
            touched = true
            function apply()
                if script.Disabled ~= true then
                    no = Char.HumanoidRootPart:Clone()
                    wait(.25)
                    Char.HumanoidRootPart:Destroy()
                    no.Parent = Char
                    Char:MoveTo(loc)
                    touched = false
                end end
            if Char then
                apply()
            end
        end
    end
end)
repeat wait() until Char
loc = Char.HumanoidRootPart.Position
Char:MoveTo(box.Position + Vector3.new(0,.5,0))
end)

Tab2Section:NewButton("Keyboard","Pc Like Keyboard",function()
loadstring(game:HttpGet(('https://raw.githubusercontent.com/manimcool21/Keyboard-FE/main/Protected%20(3).lua'),true))()
end)
