-- Create a table to store the saved variables
MyArenaNotifier = MyArenaNotifier or {}

-- Frame to handle events
local frame = CreateFrame("Frame")
frame:RegisterEvent("UPDATE_BATTLEFIELD_STATUS")

local function updateSavedVariables(status)
    MyArenaNotifier.queued = status
    -- Mark the variables to be saved
    MyArenaNotifier.lastUpdate = time()
end

frame:SetScript("OnEvent", function(self, event, ...)
    if event == "UPDATE_BATTLEFIELD_STATUS" then
        local status = GetBattlefieldStatus(1)
        if status == "confirm" then
            updateSavedVariables(true)
        else
            updateSavedVariables(false)
        end
    end
end)