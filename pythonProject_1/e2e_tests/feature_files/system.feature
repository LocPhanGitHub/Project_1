Feature: System
  Scenario: As the system, I want to rejects failed login
    Given the user is on the login page
    When the user enters wrong username in the username input box
    When the user enters wrong password in the password input box
    When the user clicks the submit button
    Then the user should not be logged in and an alert should arise to indicate that login failed

  Scenario: As the system, I want to rejects negative values for the requests
    Given the employee is on the employee homepage
    When the employee enters his user id into the id input section
    When the employee enters a name into the expense name input
    When the employee enters a negative amount into the amount input
    When the employee enters a reason into the reason input
    When the employee enters the status of the request
    When the employee enters blank for the manager comment
    When the employee clicks the submit reimbursement button to create reimbursement
    Then A pop up alert should inform the employee their request has not been made, and there was an error about negative values

  Scenario: As the system, I want to rejects non-numeric values for the requests
    Given the employee is on the employee homepage
    When the employee enters his user id into the id input section
    When the employee enters a name into the expense name input
    When the employee enters an non-numeric amount into the amount input
    When the employee enters a reason into the reason input
    When the employee enters the status of the request
    When the employee enters blank for the manager comment
    When the employee clicks the submit reimbursement button to create reimbursement
    Then A pop up alert should inform the employee their request has not been made, and there was an error about non-numeric values amount entered
