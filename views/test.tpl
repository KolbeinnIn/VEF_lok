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
        %for i in asd:
            %for x in range(1):
                <p>{{i[x+1]}} verð: {{i[x+2]}}</p>
                <br>
            %end
        % end
  </main>
</body>
</html>