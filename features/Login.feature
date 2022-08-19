Feature: Login

Scenario: Login in admin panel
  Given I go to login page
  When I fill login form
  When Submit login form
  Then I was redirected to home page as logged in user