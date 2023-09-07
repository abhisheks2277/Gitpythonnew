#created by owner at 1/9/23

Feature: Verify if Books are added and deleted using Library API


  @library
  Scenario: Verify AddBook API functionality
    Given the Book details WHich needs to be added to Library
    When we execute the Addbook PostAPI method
    Then book is successfully added
    And status code of response should be 200

    @library
    Scenario Outline: Verify AddBook API functionality
    Given the Book details with <isbn> and <aisle>
    When we execute the Addbook PostAPI method
    Then book is successfully added
      Examples:
        |isbn  |aisle |
        |fdfeee|9897  |
        |psoe  | 98297|

