-- Ensure the SavedVariables table exists
MyArenaNotifierDB = MyArenaNotifierDB or {}

-- Create a frame to listen for events
local frame = CreateFrame("Frame")

-- Register the PLAYER_LOGIN event
frame:RegisterEvent("PLAYER_LOGIN")

-- Set the script to run when the event fires
frame:SetScript("OnEvent", function(self, event, ...)
    if event == "PLAYER_LOGIN" then
        -- Debug print to see if the event triggers
        print("Player has logged in!")

        -- Set the queued variable to true
        MyArenaNotifierDB.queued = true

        -- Debug print to confirm the variable is set
        print("MyArenaNotifierDB.queued set to true")
    end
end)
