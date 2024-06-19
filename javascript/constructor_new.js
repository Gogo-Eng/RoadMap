function createPerson(name) {
    this.name = name;
    this.introduceSelf = function () {
      console.log(`Hi! I'm ${this.name}.`);
    };
  }

const salva = new createPerson("Salva");
salva.introduceSelf();
// "Hi! I'm Salva."

const frankie = new createPerson("Frankie");
frankie.introduceSelf();
// "Hi! I'm Frankie."

const myNotification = new Notification("Hello!");
