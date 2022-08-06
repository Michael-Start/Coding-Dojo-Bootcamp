import Person from './components/Person';
import './App.css';

function App() {
  return (
    <div className="App">
      <Person person = {['Doe', 'Jane', 44 , 'Black']}/>
      <Person person = {['Smith', 'John', 55 , 'Red']}/>
      <Person person = {['Kid', 'Billy', 24 , 'Brown']}/>
      -<Person person = {['Blargle', 'Smargle', 244 , 'Green']}/>
    </div>
  );
}

console.log(Person)
export default App;
