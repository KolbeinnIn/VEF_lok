%rebase('base.tpl')
<h1>Karfa</h1>
<div>
    % if len(karfa) <= 0:
        <p>Það eru engar vörur í körfu</p>
        <p><a href="/">Versla meira</a></p>
    % else:
        % for i in range(len(karfa)):
            <p><a href="/karfa/{{karfa[i]}}">{{karfa[i]}}</a><p>
        % end
    <p style="padding-top:14px;">Samtals: {{verd}}kr</p>
    <p><a href="/">Versla meira</a></p>
    <p><a href="/karfa/eyda">Fjarlægum allar vörur úr körfu</a></p>
</div>
