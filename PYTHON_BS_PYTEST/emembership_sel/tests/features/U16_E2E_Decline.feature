Feature: Under 16 - New volunteer + District manager declines application

			pytest.mark.T1165

			Scenario: Under 16 declines application - New volunteer - Verify Email

						Given User is on "rfsRoleExplorer" page
						Then User clicks "ApplyToVolunteer" button
						And User then clicks "CreateProfile" button
						Then User Enter Details and Submit details to create profile "data/newProfileDetails16.json"
						Then user is displayed with message to verify email

			Scenario: Under 16 declines application - Service Now - Search Email & Verifies

						Given User is on "Service Now - EMAILS" page
						When User enters valid credentials "username" "password"
						Then User searches for email and verifies

			Scenario: Under 16 declines application -
						Given User is on "login" page
						When Candidate enters credentials "Email" "password"
						Then User click "new" application button
						And Verify the forms displayed for "under16"
						When candidate clicks the apply volunteer card for "U16"
						And clicks continue
						Then candidate fills in junior volunteer details "data/volunteerDetails_U16.json"
						Then candidate is displayed with message about successful submission
						Then  saves app ref to JSON file

			Scenario: Under 16 declines application - ServiceNow - Search submission approval email for "application"
						Given User is on "Service Now" page
						When User enters valid credentials "username" "Password"
						Then User clicks on user profile and select impersonate user
						Then User search for "anirudh.kodhandaswamy@rfs.nsw.gov.au"
						Then user search for confirmation email for "application"

			Scenario:  Under 16 declines application - First stage - Brigade Approval
						Then User clicks on user profile and select impersonate user
						Then User search for "DrewButters-vol@rfs.nsw.gov.au"
						Then User logs in service now portal for "brigade" "approval"

			Scenario: Under 16 declines application - Search approval email for "brigade"
						Then User clicks on user profile and select impersonate user
						Then User search for "anirudh.kodhandaswamy@rfs.nsw.gov.au"
						Then user search for confirmation email for "brigade"

			Scenario: Under 16 declines application -  Second stage district decline
						Then User clicks on user profile and select impersonate user
						Then User search for "Jim.Darrant@rfs.nsw.gov.au"
						Then User logs in service now portal for "district" "decline"

			Scenario: Under 16 declines application -
						Then User clicks on user profile and select impersonate user
						Then User search for "anirudh.kodhandaswamy@rfs.nsw.gov.au"
						Then user search for confirmation email for "district"

			Scenario: Under 16 declines application -
						Then User clicks on user profile and select impersonate user
						Then User search for "External.Automation@rfs.nsw.gov.au"
						Then the status of the application is verified
