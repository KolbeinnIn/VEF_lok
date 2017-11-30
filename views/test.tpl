<!DOCTYPE html>
<html>
<head>
    <intercept-url pattern="/favicon.ico" access="ROLE_ANONYMOUS" />
    <title>Verkefni 8</title>
    <meta charset="utf-8">
    <link href="/static/css/styles.css" rel="stylesheet" type="text/css">
</head>
<body>
   <main>
       <header>
            <h1>Vefverslun</h1>
       </header>
        % for i in asd:
            %for x in i:
                <p>{{i[x]}}</p>
        % end
  </main>
</body>
</html>