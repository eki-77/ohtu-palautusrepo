*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  erkki
    Set Password  newpassword
    Click  button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  newpassword
    Click  button >> text=Register
    Register Should Fail With Message  Userame is too short, 3 characters required 

Register With Valid Username And Too Short Password
    Set Username  erkki
    Set Password  kone
    Click  button >> text=Register
    Register Should Fail With Message  Password is too short, 8 characters required 


Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  newpassword
    Click  button >> text=Register
    Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Register Should Succeed
    Welcome Page Should Be Open

