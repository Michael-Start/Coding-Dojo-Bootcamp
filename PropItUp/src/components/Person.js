import React, {useState} from 'react'


const Person = (props) =>{
    const{person:[last_name, first_name, age, hair_color]} = props
    const [stateAge, setStateAge] = useState(age);
    return (
        <div>
            <h1>{last_name}, {first_name} </h1>
            <p>Age: {stateAge}</p>
            <p>Hair color: {hair_color}</p>
            <button onClick ={ (event) => setStateAge(stateAge+1)}>Happy Birthday {first_name} {last_name}!</button>
            
        </div>
    );
    };
export default Person