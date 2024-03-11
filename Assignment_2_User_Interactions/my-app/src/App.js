
import './App.css';

function App() {
  return (
   <div classname="App">
      <header classname="App-header">
        <div style={{ fontFamily: "'Franklin Gothic Medium', sans-serif" }}>
          <h1 style={{ backgroundColor: 'rgb(0, 150, 255)' }}>About Me</h1>
          <h3>Introduction</h3>
          <p style={{ fontfamily: " 'Franklin gothic medium', sans-serif"}}>
           Hi, my name is Jasmin and I am a second year student here at CSUSB. I am currently pursuing my B.S. in Computer Science.
          </p>
          <h3>A hobby of mine</h3>
          <p style={{ fontfamily: " 'Franklin gothic medium', sans-serif"}}>
           One of my favorite things to do is read. I just finished my first book of 2024, it was Slaughterhouse-Five, or The Children's Crusade: A Duty-Dance with Death, by Kurt Vonnegut. The title next on my list is Invincible Compendium Volume 1 by Robert Kirkman and Ryan Ottley. I am currently on page 518 and can't wait to keep reading. It is an engrossing read thus far. 😍 📚
          </p>
          <h3>One more hobby</h3>
          <p style={{ fontfamily: " 'Franklin gothic medium', sans-serif"}}>
           Another one of my hobbies is cooking and baking. The latest meal I made was kung pao chicken, chow mein,
           and shrimp fried rice. I served the plate with steamed broccoli as well, it was delightful. And the latest dessert I made was crème brûlée. I love crème brûlée so much, I make it often.
           But the last time I made it I could not find my torch so I used a hot spoon to melt the sugar onto the custard and it worked quite well actually. I was pleasantly surprised. 😋
          </p>
          <h2>List of some of my favorites</h2>
          <ul style={{ listStyle: 'none', padding: 0 }}>
            <li style={{ border: '1px solid #088F8F', padding: '6px', margin: '2px' }}>Icecream: Chocolate</li>
            <li style={{ border: '1px solid #088F8F', padding: '6px', margin: '2px' }}>Color: Blue &#128153;</li>
            <li style={{ border: '1px solid #088F8F', padding: '6px', margin: '2px' }}>Book: Fight Club</li>
            <li style={{ border: '1px solid #088F8F', padding: '6px', margin: '2px' }}>Song: Lovelier Girl by Beach House</li>
            <li style={{ border: '1px solid #088F8F', padding: '6px', margin: '2px' }}>Movie: Luca</li>
          </ul>

          <div>
            <img src="/crèmebrûlée.jpg" alt="Crème brûlée" />
          </div>

          <div>
          <p>
           Here is a link that directs you to my main Github account: <a href="https://github.com/jasflor">Jasmin's Main Github account</a>
          </p>
        </div>

        <p style={{ fontSize: '30px' }}> &#128512; &#128151; &#128512; &#128151;</p>
      </div>
    </header>
  </div>
  );
}

export default App;
