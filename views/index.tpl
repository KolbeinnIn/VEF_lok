        % rebase("base.tpl")
        <h2>Veldu vöru í körfu!</h2>
        <div>
            % for i in range(len(vorur)):
               <p><a href="/karfa/baeta/{{vorur[i]['voruid']}}">{{vorur[i]['name']}}</a></p>
            % end
            <p>Þú hefur skoðað síðuna: {{teljari}} sinnum</p>
        </div>
