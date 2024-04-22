% Define the paths to your GDF files
gdf_files = {
    'D:\porojects\EEG classification\datasets\BCICIV_2a_gdf\A01T.gdf',
    'D:\porojects\EEG classification\datasets\BCICIV_2a_gdf\A02T.gdf',
    'D:\porojects\EEG classification\datasets\BCICIV_2a_gdf\A03T.gdf',
    'D:\porojects\EEG classification\datasets\BCICIV_2a_gdf\A04T.gdf',
    'D:\porojects\EEG classification\datasets\BCICIV_2a_gdf\A05T.gdf',
    'D:\porojects\EEG classification\datasets\BCICIV_2a_gdf\A06T.gdf',
    'D:\porojects\EEG classification\datasets\BCICIV_2a_gdf\A07T.gdf',
    'D:\porojects\EEG classification\datasets\BCICIV_2a_gdf\A08T.gdf',
    'D:\porojects\EEG classification\datasets\BCICIV_2a_gdf\A09T.gdf'
};


for i = 1:numel(gdf_files)
    
    [s, h] = sload(gdf_files{i}, 0, 'OVERFLOWDETECTION:OFF');
    
    % Extract type, pos, and dur data
    type = h.EVENT.TYP;
    pos = h.EVENT.POS;
    dur = h.EVENT.DUR;
    
    % Write data to Excel file with each type, pos, and dur in different columns
    filename = sprintf('2aEvents\\A0%dT.xlsx', i);
    data = [type, pos, dur];
    xlswrite(filename, data);
end



