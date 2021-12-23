Feature: Managers Interact with Reimbursements
  Scenario: As an manager, I want to login to my manager homepage
    Given the user is on the login page
    When the manager enters their username in the username input box
    When the manager enters their password in the password input box
    When the manager chose manager from dropbox
    When the manager clicks the submit button
    When the manager were redirected to manager home page
    Then the manager should be logged in

  Scenario: As an manager, I to manage my reimbursements
    Given the manager is on the manager homepage
    When the manager enters the request id into the request id input section
    When the manager enters the user id into the id input section
    When the manager enters the name into the expense name input
    When the manager enters the amount into the amount input
    When the manager enters the reason into the reason input
    When the manager edits the status of the request
    When the manager enters the manager comment
    When the manager clicks the submit reimbursement button to update the reimbursement
    Then A pop up alert should inform the manager the request has been updated

  Scenario: As an user, I want to logout after I'm done
    Given the user is on their homepage
    When the user clicks the logout button
    When the user were redirected back to their login page
    Then the user should be logged out