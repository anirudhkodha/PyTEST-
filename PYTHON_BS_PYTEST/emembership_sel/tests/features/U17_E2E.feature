Feature: Under 17 applicant E2E

			@T1163
			Scenario: Under 17 applicant E2E
						Given User is on "rfsRoleExplorer" page
						Then User clicks "ApplyToVolunteer" button
						And User then clicks "CreateProfile" button
						Then User Enter Details and Submit details to create profile "data/newProfileDetails17.json"
						Then user is displayed with message to verify email
						Given User is on "Service Now" page
						When User enters valid credentials "username" "Password"
						Then User searches for email and verifies
						Given User is on "login" page
						When Candidate enters credentials "Email" "password"
						Then User click "new" application button
						And Verify the forms displayed for "under17"
						When candidate clicks the apply volunteer card for "U16"
						And clicks continue
						Then candidate fills in junior volunteer details "data/volunteerDetails_U17.json"
						Then candidate continues to police check
						Then candidate fills in police check details for U17 "data/policeChkDetails.json"
						Then candidate is displayed with message about successful submission
						Then candidate saves app ref to JSON file
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



