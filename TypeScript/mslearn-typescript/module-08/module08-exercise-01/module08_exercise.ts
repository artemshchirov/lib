namespace AllGreetings {
  export namespace Greetings {
    export function returnGreeting(greeting: string) {
      console.log(`The message from namespace Greetings is ${greeting}.`);
    }
  }
  export namespace GreetingsWithLength {
    export function returnGreeting(greeting: string) {
      let greetingLength = getLength(greeting);
      console.log(`The message from namespace GreetingsWithLength is ${greeting}. It is ${greetingLength} characters long.`);
    }
    function getLength(message: string): number {
      return message.length
    }
  }

  // returnGreeting('Hello');                     // Returns error
  Greetings.returnGreeting('Bonjour');         // OK
  GreetingsWithLength.returnGreeting('Hola');  // OK
}

AllGreetings.Greetings.returnGreeting('Bonjour');        // OK
AllGreetings.GreetingsWithLength.returnGreeting('Hola');  // OK

import greet = AllGreetings.Greetings;
greet.returnGreeting('Bonjour');

console.log('greet: ', greet);
console.log('AllGreetings: ', AllGreetings);