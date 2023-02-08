<!DOCTYPE html>
<html>
    <head>
        <title>Astatine.shop : Login</title>
        <script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <link rel="icon" type="image/x-icon" href="/favicon.ico">
        <link rel="stylesheet" href="./styles/style.css">
        <link rel="stylesheet" href="./styles/login.css">
    </head>
    <body>
        <div style="height:100vh; width:100vw; padding:0; margin:0; display:flex; justify-content:center; align-items:center;">
            <div class="parent signup">
                <h1>
                    astatine.shop
                </h1>
                <form class="login" method="POST">
                    <div id="fields">
                        <h2>Name : </h2>
                        <input type="text" name="name">
                        <h2>Username : </h2>
                        <input type="text" name="username">
                        <h2>Password : </h2>
                        <input type="password">
                        <h2>Confirm password : </h2>
                        <input type="password" name="password">
                    </div>
                    <a id="login" href="/login.php">
                        Back to login
                    </a>
                    <input id="submit" type="submit" value="Sign up">
                </form>
            </div>
        </div>

        <script src="./scripts/main_script.js"></script>
    </body>
</html>