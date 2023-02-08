<div class="nav-bar">
    <h1 class="title">
        <a href="index.php">
            astatine.shop
        </a>
    </h1>
    <!-- <div class="query">
        <input type="text" placeholder="What do you fancy?">
    </div> -->
    <div id="sections">
        <!-- <a href="#">
            <img src="assets/logos/search.png">
        </a> -->
        <a href="#">
            <img src="assets/logos/cart.png">
        </a>
        <?php
        echo isset($_COOKIE["user_id"]) ? "
        <a href='#'>
            <img src='assets/logos/profile.png'>
        </a>" :
        "<a id='login-button' href='../login.php'>
            <h3>
                Log in
            </h3>
        </a>"
        ?>
    </div>
</div>