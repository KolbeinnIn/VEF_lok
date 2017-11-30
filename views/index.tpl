        % rebase("base.tpl")
        <h2>Veldu vöru í körfu!</h2>
        <div>
            %for i in asd:
                %for x in range(1):
                    <p><a href="/karfa/baeta/{{i[0]}}">{{i[x+1]}} verð: {{i[x+2]}}</a></p>
                    <br>
                %end
            % end
            <a href="/karfa">Karfan þín</a>
            <p>Þú hefur skoðað síðuna: {{teljari}} sinnum</p>
        </div>
