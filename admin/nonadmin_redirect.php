<!DOCTYPE html>
<html>
    <head>
        <title>Bukan admin</title>
        <link rel="stylesheet" href="../styles/style.css">
        <link rel="stylesheet" href="../styles/admin/nonadmin_redirect.css">
        <script>
            var time = 3;
            setInterval(() => {
                time--;
                if (time <= 0) {
                    window.location.href = '../index.php';
                }
            }, 1000);
        </script>
    </head>
    <body>
        <h1>Akses kepada laman ini tidak dibenarkan kerana anda bukan seorang admin.</h1>
        <h1>Anda akan dialamatkan semula ke laman utama sebentar lagi.</h1>
        <a href="../index.php">Tekan pautan ini jika tidak dialamatkan semula secara automatik.</a>
    </body>
</html>