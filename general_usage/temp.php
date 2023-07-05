<?php
session_start();
// database info
$DATABASE_HOST = 'localhost';
$DATABASE_USER = 'root';
$DATABASE_PASS = '';
$DATABASE_NAME = 'etunapicker';

// connecting to database
$con = mysqli_connect($DATABASE_HOST, $DATABASE_USER, $DATABASE_PASS, $DATABASE_NAME);
if ( mysqli_connect_errno() ) {
    // text if error occurs
	exit('Pangkalan data tidak dapat dicapai!' . mysqli_connect_error());
}

echo isset($_POST['filesubmit']);

if(isset($_POST['filesubmit'])){
    
    // Allowed mime types
    $csvMimes = array(
        'text/x-comma-separated-values',
        'text/comma-separated-values',
        'application/octet-stream',
        'application/vnd.ms-excel',
        'application/x-csv',
        'text/x-csv',
        'text/csv',
        'application/csv',
        'application/excel',
        'application/vnd.msexcel',
        'text/plain'
    );

    // Validate whether selected file is a CSV file

    echo 'is empty' . empty($_FILES['file']['name']);
    echo 'in array' . in_array($_FILES['file']['type'], $csvMimes);

    if(!empty($_FILES['file']['name']) && in_array($_FILES['file']['type'], $csvMimes)){
        
        // If the file is uploaded
        if(is_uploaded_file($_FILES['file']['tmp_name'])){

            // Open uploaded CSV file with read-only mode
            $csvFile = fopen($_FILES['file']['tmp_name'], 'r');
            
            // Skip the first line
            fgetcsv($csvFile);
            
            // Parse data from CSV file line by line
            while(($line = fgetcsv($csvFile)) !== FALSE){
                // Get row data
                $koditem = $line[0];
                $jenama = $line[1];
                $namaitem = $line[2];
                $beratitem = $line[3];
                $hargaitem = $line[4];
                
                // Check whether item already exists in the database with the same code
                $prevQuery = "SELECT Nama_Item FROM item WHERE Kod_Item = '".$line[1]."'";
                $prevResult = $db->query($prevQuery);
                
                if($prevResult->num_rows > 0){
                    // Update member data in the database
                    $db->query("UPDATE item SET Jenama = '".$jenama."', Nama_Item = '".$namaitem."', Berat_Item = '".$beratitem."', Harga = '".$hargaitem."', WHERE Kod_Item = '".$koditem."'");
                }else{
                    // Insert member data in the database
                    $db->query("INSERT INTO item (Kod_Item, Jenama, Nama_item, Berat_Item, Harga) VALUES ('".$koditem."', '".$jenama."', '".$namaitem."', '".$beratitem."', '".$hargaitem."')");
                }
            }
            
            // Close opened CSV file
            fclose($csvFile);
            
            echo "<script>alert('Import fail CSV berjaya!')</script>";
        }else{
            echo "<script>alert('Import fail CSV gagal, cuba lagi!')</script>";
        }
    }
}
?>