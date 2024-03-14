Feature: Adult E2E

			@T1167
			Scenario: Adult E2E - Applying for transfer to another brigade
						Given User is on "Service Now" page
						When User enters valid credentials "anirudhk" "Wildfire20!"
						Then User clicks on user profile and select impersonate user
						Then User search for "CallumCarey-vol@rfs.nsw.gov.au"
						Then User logs in service now portal for transfer application
						Then User click "new" application button
						And Verify the forms displayed for "adultRejoin"
						When User clicks the Apply for Transfer to another brigade card
						And clicks continue
						Then User fills in volunteer details "data/volunteerDetails_Adult_FF.json"
						Then User continues to police check
						Then User fills in police check details "data/policeChkDetails.json"
						Then candidate is displayed with message about successful submission
						Then User saves app ref to JSON file

#     Scenario: Service now E2E brigade
#        Given User is on "Service Now" page
#        When User enters valid credentials "anirudhk" "Wildfire20!"
#        Then User clicks on user profile and select impersonate user
#        Then User search for "DrewButters-vol@rfs.nsw.gov.au"
#        Then User logs in service now portal for brigade approval


			@serviceNowE2E
			Scenario: Service now E2E district
#        Given User is on "Service Now" page
#        When User enters valid credentials "anirudhk" "Wildfire20!"
#        Then User clicks on user profile and select impersonate user
#        Then User search for "Jim.Darrant@rfs.nsw.gov.au"
#        Then User logs in service now portal for district approval
#
#  @serviceNowE2E @abc
#    Scenario: Service now E2E police check
#        Given User is on "Service Now" page
#        When User enters valid credentials "anirudhk" "Wildfire20!"
#        Then User logs in service now portal for closing policeCheck task
###
##    @serviceNowE2E
#    Scenario: Service now E2E service check
#        Given User is on "Service Now" page
#        When User enters valid credentials "anirudhk" "Wildfire20!"
#        Then User logs in service now portal for closing serviceCheck task for dual

