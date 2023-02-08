class User {
    static collection = [];

    constructor (name, username, password) {
        this.id = User.collection.length;

        this.name = name;

        this.username = username;
        this.password = password;
    }

    static initialize() {
        User.collection.push(new User("lorem", "lorem_ipsum", "1234"));
        User.collection.push(new User("ipsum", "lorem_uwu", "1234"));

        // fetch from sql here
        

        console.log(User.authorizeSignIn("lorem_ipsum", "1234"));
        console.log(User.authorizeSignIn("lorem_ipsum", "idk"));
    }

    static fetchUser(username) {
        return User.collection.find(n => n.username == username);
    }

    static authorizeSignIn(username, password) {
        var result = User.collection.find(n => n.username == username);
        if (result != undefined) {
            if (result.password == password) {
                return SignInResult.Success;
            } else {
                return SignInResult.WrongPassword;
            }
        } else {
            return SignInResult.NoAccount;
        }
    }
}

const SignInResult = {
    Success : 0,
    NoAccount : -1,
    WrongPassword : -2,
    Generic : 404
}