Feature: Employees Interact with Reimbursements
  Scenario: As an employee, I want to login to my employee homepage
    Given the user is on the login page
    When the user enters their username in the username input box
    When the user enters their password in the password input box
    When the user chose employee from dropbox
    When the user clicks the submit button
    When the user were redirected to employee home page
    Then the user should be logged in

  Scenario: As an employee, I want to manage my reimbursements
    Given the employee is on the employee homepage
    When the employee enters his user id into the id input section
    When the employee enters a name into the expense name input
    When the employee enters an amount into the amount input
    When the employee enters a reason into the reason input
    When the employee enters the status of the request
    When the employee enters blank for the manager comment
    When the employee clicks the submit reimbursement button to create reimbursement
    Then A pop up alert should inform the employee their request has been made

  Scenario: As an user, I want to logout after I'm done
    Given the user is on their homepage
    When the user clicks the logout button
    When the user were redirected back to their login page
    Then the user should be logged out
