import React, {useState} from 'react'

const Form = () =>{
    const[first_name, setfirst_name] =useState("");
    const[last_name, setlast_name] = useState("");
    const[email, setEmail] = useState("");
    const[password, setPassword] = useState("");
    const[confirm_password, setConfirm_password] = useState("");




    return(
        <div>
            <h1>Create a User in Real Time!</h1>
            <form onSubmit>
                <div>
                    <label htmlFor = 'first_name'>First Name: </label>
                    <input type = 'text' name = 'first_name' onChange={(e)=> setfirst_name(e.target.value)}/>
                    {first_name.length < 2 && first_name.length > 0?(
                        <p>First Name must be at least 2 characters!</p>):
                        ('')
                    }
                    
                </div>
                <div>
                    <label htmlFor='last_name'>last Name: </label>
                    <input type="text" name='last_name' onChange={(e)=> setlast_name(e.target.value)} />
                    {last_name.length < 2 && last_name.length > 0?(
                        <p>Last Name must be at least 2 characters!</p>):
                        ('')
                    }
                    
                </div>
                <div>
                    <label htmlFor='email'>Email: </label>
                    <input type="text" name='email' onChange={(e)=> setEmail(e.target.value)} />
                    {email.length < 5 && email.length > 0?(
                        <p>Email must be at least 5 characters!</p>):
                        ('')
                    }
                    
                </div>
                <div>
                    <label htmlFor='password'>Password: </label>
                    <input type="password" name = 'password' onChange={(e) => setPassword(e.target.value)} />
                    {password.length < 8 && password.length > 0?(
                        <p>Password must be at least 8 characters!</p>):
                        ('')
                    }
                    
                </div>
                <div>
                    <label htmlFor='confirm_password'>Confirm Password</label>
                    <input type="password" name = 'confirm_password' onChange={(e) => setConfirm_password(e.target.value)} />
                    {confirm_password.length < 8 && confirm_password.length >= 0?(
                        ('')
                    ):
                    
                    confirm_password === password?(
                        <p>'Passwords match!'</p>):
                        (<p>Passwords must match!</p>)
                    
                    }
                </div>
                <div>
                    <input type="submit" value = 'Create User' />
                </div>
            </form>
            <div>
                <div>
                    <label>First Name: </label>{first_name}
                </div>
                <div>
                    <label>Last Name: </label>{last_name}
                </div>
                <div>
                    <label>Email: </label> {email}
                </div>
                <div>
                    <label>Password: </label>{password}
                </div>
                <label>Confirm Password:</label>{confirm_password}
            </div>
        </div>

    );
};

export default Form;