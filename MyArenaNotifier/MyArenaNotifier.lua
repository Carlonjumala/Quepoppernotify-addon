-- Ensure the SavedVariables table exists
MyArenaNotifierDB = MyArenaNotifierDB or {}

-- Create a frame to listen for events
local frame = CreateFrame("Frame")

-- Register the ADDON_LOADED and PLAYER_LOGIN events
frame:RegisterEvent("ADDON_LOADED")
frame:RegisterEvent("PLAYER_LOGIN")

frame:SetScript("OnEvent", function(self, event, arg1)
    if event == "ADDON_LOADED" and arg1 == "MyArenaNotifier" then
        -- When the addon is loaded, initialize saved variables if they do not exist
        if MyArenaNotifierDB.queued == nil then
            MyArenaNotifierDB.queued = false
            print("Addon loaded for the first time.")
        end
    elseif event == "PLAYER_LOGIN" then
        -- When the player logs in, set the queued variable to true and save
        MyArenaNotifierDB.queued = true
        print("Player has logged in!")
        print("MyArenaNotifierDB.queued set to true")
    end
end)
