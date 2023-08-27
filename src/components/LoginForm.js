import React from 'react';
export const LoginForm = () => {
  return (
    <div className="login-container">
      <h1>Login Form</h1>
      <input type= "email" placeholder="Email address" id = "text"/>
      <input type= "password" placeholder="Password" id ="text"/>
      <input type= "button" value="Submit" id = "button"/>
    </div>
  )
}
