import logo from './logo.svg';
import './App.css';
import cat from "./images/cat_standing.png"

function App() {
  return (
    <div className="Website">



      <div className="Sub-website">
        <div class = "web1container">
        <h1>About Diego Ozuna</h1>
        <p id = "message">
            Hello everyone, 
            My name is Diego Ozuna, I am a senior here at CSUSB and will graduate in December 2024.
            I am majoring in Computer Science with a minor in Mathematics. Since transfering, I have been on the Dean's
            List. I want to work closely with Machine Learning and AI which is why I am interested mostly in the field of Data Science.
        </p>
        <p>
            My hobbies are film photography and video games. I like to play first-person shooters, MOBAs,
            and some survival games. My interest in photography comes from a class I took in highschool.
        </p>
        <p>
            If you have questions about stuff in Comp Sci or Math I will try to help, as helping others also helps me. :)
        </p>

        <div class="highlightGIT">
            <a href="https://github.com/DiegoOzuna/Platform-Computing">My GITHUB Page</a>
        </div>

        <div>
            <p>Here is a list of my classes below...</p>
            <ol class = "listClass">
                <li>CSE 4310 : Algorithm Analysis</li>
                <li>CSE 4500 : Platforming Computing</li>
                <li>CSE 5000 : Formal Languages and Automata</li>
                <li>CSE 5120 : Intro Artificial Intelligence</li>
                <li>CSE 5250 : Parallel Algorithms</li>
                <li>CSE 5953 : Independent Study</li>
            </ol>
            <p>Two of my classes are online, the others are in person Monday and Wednesday.
            </p>
        </div>
        <img src={cat} alt="cat" class="center"/>
        <input name="my-text" placeholder="hello"></input>
        <button name="button">Hello</button>
        </div>
      </div>



      <div className="Sub-website">
        <div class = "web2container">
        <h2>About Jasmin</h2>
        <p id = "mine"> 
            Hi, my name is Jasmin Flores. And I am a student at CSUSB. Moreover, I am pursuing my B.S. in Computer Science.
        </p>
        <p>
            One of my favorite things to do is read. I just finished Slaughterhouse-Five, or The Children's Crusade: A Duty-Dance with Death, by Kurt Vonnegut. 
            My next title is Invincible Compendium Volume 2 by Robert Kirkman and Ryan Ottley.
        
        </p>
        <p>
            Another one of my hobbies is baking. The latest dessert I made was crème brûlée, I make it often. But the last time I made it I could not find my torch 
            so I used a hot spoon to melt the sugar onto the custard and it worked quite well actually. I was pleasantly surprised.
        </p>

        <div>
            <h2>List of some of my favorites</h2>
            <ul style = "listStyle">
                <li>Color: Blue &#128160;</li>
                <li>Book: Fight Club by Chuck Palahniuk</li>
                <li>Song: Lovelier Girl by Beach House</li>
                <li>Movie: Asteroid City directed by Wes Anderson</li>
            </ul>
        </div>

        <div class="myLink">
            Here is a link that directs you to my main Github account: <a href="https://github.com/jasflor">Jasmin's Main Github account</a>
        </div>

        <div>
            <img src="/crèmebrûlée.jpg" alt="Crème brûlée" />
        </div>
      </div>



      <div className="Sub-website">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Content of website 3
          </p>
        </header>
      </div>




      <div className="Sub-website">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Content of website 4
          </p>
        </header>
      </div>




    </div>
  );
}

export default App;