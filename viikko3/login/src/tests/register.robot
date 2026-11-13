*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  erkki
    Set Password  newpass123
    Click  button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  newpass123
    Click  button >> text=Register
    Register Should Fail With Message  Userame is too short, 3 characters required 

Register With Valid Username And Too Short Password
    Set Username  erkki
    Set Password  kone
    Click  button >> text=Register
    Register Should Fail With Message  Password is too short, 8 characters required 


Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  newpass123
    Click  button >> text=Register
    Register Should Fail With Message  User with username kalle already exists

Register With Password Containing Letters And Digits
    Set Username  erkki
    Set Password  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Letters And Special Character
    Set Username  erkki
    Set Password  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Only Lowercase Letters
    Set Username  erkki
    Set Password  kallekalle
    Click  button >> text=Register
    Register Should Fail With Error Message

Register With Password Containing Only Uppercase And Lowercase Letters
    Set Username  erkki
    Set Password  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Error Message

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Register Should Fail With Error Message
    Register Page Should Be Open
    ${message}=  Get Text  css=ul li
    Should Not Be Empty  ${message}

Register Should Succeed
    Welcome Page Should Be Open
