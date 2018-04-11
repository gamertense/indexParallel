<html>

<head>
    <?php require_once('bootstrap.php') ?>
    <script src="vendor/lightbox/js/lightbox.min.js"></script>
    <link rel="stylesheet" href="vendor/lightbox/css/lightbox.min.css">
    <style>
        @import url(https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css);
        @import url(https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.4.3/css/mdb.min.css);

        .hm-gradient {
            background-color: #eee;
        }

        .darken-grey-text {
            color: #2E2E2E;
        }
    </style>
    <title>Search Parallel</title>
</head>

<body>
<?php
if (isset($_POST['term1']) && isset($_POST['term2'])) {
    $term1 = $_POST['term1'];
    $term2 = $_POST['term2'];
    chdir('python_script'); //Change directory
    $command = escapeshellcmd("python3 index.py $term1 $term2");
    $output = shell_exec($command);
}
?>
<form method="post">
    <div class="container mt-4">
        <div class="text-center darken-grey-text mb-4">
            <h1 class="font-bold mt-4 mb-3 h5">Input search term 1</h1>
            <div class="form-group">
                <div class="col-md-6 offset-md-3">
                    <input type="text" name="term1" value="brother">
                    <label>For example: brother</label>
                </div>
            </div>
        </div>
        <div class="text-center darken-grey-text mb-4">
            <h1 class="font-bold mt-4 mb-3 h5">Input search term 2</h1>
            <div class="form-group">
                <div class="col-md-6 offset-md-3">
                    <input type="text" name="term2" value="water">
                    <label>For example: water</label>
                </div>
            </div>
            <button class="btn btn-success">Search <i class="fa fa-search"></i>
        </div>
        <?php
        if (isset($output)) {
            ?>
            <h1 class="text-center font-bold mt-4 mb-3 h5">Output</h1>
            <div class="col-md-8 mb-4 offset-md-2">
                <div class="card">
                    <div class="card-block p-3">
                        <?php
                        echo $output;
                        ?>
                    </div>
                </div>
            </div>
            <?php
        }
        ?>
        <div class="text-center darken-grey-text mb-4">
            <h1 class="font-bold mt-4 mb-3 h5">Benchmark graph</h1>
            <div class="col-md-8 mb-4 offset-md-2">
                <div class="card">
                    <center>
                        <div id="imagediv"><a href="python_script/benchmark.png" data-lightbox="image-1"
                                              data-title="Serial vs. Multiprocessing"></a></div>
                    </center>
                </div>
            </div>
        </div>
    </div>
</form>
</body>

<script>
    var img = $("<img />").attr('src', 'python_script/benchmark.png')
        .on('load', function () {
            if (!this.complete || typeof this.naturalWidth == "undefined" || this.naturalWidth == 0) {
                alert('broken image!');
            } else {
                $("#imagediv a").append(img);
                document.getElementsByTagName("img")[0].setAttribute("width", "80%");
            }
        });
    lightbox.option({
        'resizeDuration': 200,
        'wrapAround': true
    })
</script>
