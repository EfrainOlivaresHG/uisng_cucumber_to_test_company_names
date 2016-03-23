Feature: Single word name 
  Scenario: Single word in company name 
    Given there is only one word in a company name 
    And the word is an important word 
    Then I should get a True result for identification 
