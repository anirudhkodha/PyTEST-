Feature: Adult E2E - Applying for fire fighting role, H&S = Can + H&S questions all = No + Declarations at least 1 = Yes + Special Provisions = No

			T1175

			Scenario: Adult E2E - Applying for fire fighting role, H&S = Can + H&S questions all = No + Declarations at least 1 = Yes + Special Provisions = No
						Given User is on "rfsRoleExplorer" page
						Then User clicks "ApplyToVolunteer" button
						And User then clicks "CreateProfile" button
						Then User Enter Details and Submit details to create profile "data/newProfileDetails.json"
						Then user is displayed with message to verify email
						Given User is on "Service Now" page
						When User enters valid credentials "username" "Password"
						Then User searches for email and verifies
						Given User is on "login" page
						When Candidate enters credentials "Email" "password"
						Then User click "new" application button
						And Verify the forms displayed for "adult"
						When candidate clicks the apply volunteer card for "Adult"
						And clicks continue
						Then User fills in volunteer details for "firefighting" "data/volunteerDetails_Adult_FF_DecYes.json"
						Then User continues to police check
						Then User fills in police check details "data/policeChkDetails.json"
						Then candidate is displayed with message about successful submission
						Then User saves app ref to JSON file
						Given User is on "Service Now" page
						When User enters valid credentials "username" "Password"
						Then User clicks on user profile and select impersonate user
						Then User search for "anirudh.kodhandaswamy@rfs.nsw.gov.au"
						Then user search for confirmation email for "application"
						Then User clicks on user profile and select impersonate user
						Then User search for "DrewButters-vol@rfs.nsw.gov.au"
						Then User logs in service now portal for "brigade" "approval"
						Then User clicks on user profile and select impersonate user
						Then User search for "anirudh.kodhandaswamy@rfs.nsw.gov.au"
						Then user search for confirmation email for "brigade"
						Then User clicks on user profile and select impersonate user
						Then User search for "Jim.Darrant@rfs.nsw.gov.au"
						Then User logs in service now portal for "district" "approval"
						Then User clicks on user profile and select impersonate user
						Then User search for "anirudh.kodhandaswamy@rfs.nsw.gov.au"
						Then user search for confirmation email for "district"
						Then User logs in service now portal for closing policeCheck task
						Then User logs in service now portal for closing serviceCheck task
						Then User clicks on user profile and select impersonate user
						Then User search for "External.Automation@rfs.nsw.gov.au"
						Then the status of the application is verified





