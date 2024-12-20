% Clearing to ensure we track when we want 
clear 

% Loading in the data, and storing into variables 
load('ExampleData.mat');
lat=Position.latitude;
lon=Position.longitude;
positionDatetime=Position.Timestamp;

% Setting up the acceleration variables to collect the data 
Xacc = Acceleration.X;
Yacc = Acceleration.Y;
Zacc = Acceleration.Z; 
accelDatetime=Acceleration.Timestamp;

% Obtain linear time data in time data in seconds from a datetime array 
positionTime=timeElapsed(positionDatetime);
accelTime=timeElapsed(accelDatetime); 

% Represent the circumference of the Earth in miles 
earthCirc = 24901;

% Represents the total distance traveled, starts at 0
totaldis = 0; 

% To calculate the total distance travelled 
for i = 1:(length(lat)-1)
	lat1 = lat(i);      % First latitude
	lat2 = (lat(i+1);   % Second latitude
	lon1 = lon(i);      % First longitude
	lon2 = lon(i+1);    % Second longitude 

	% hdhh
	degDis = distance(lat1, lon1, lat2, lon2);
	dis = (degDis/360)*earthCirc; 

	totaldis = totaldis + dis 

end 

% Average stride length for cats/dogs 
catstride = 0.5; 
dogstride = 1; 

% Converting steps counted from the miles to feet 
totaldis_ft = totaldis*5200;   % Average stride (ft)
catsteps = totaldis_ft/catstride     % Converting distance from miles to feet 
dogsteps = totaldis_ft/dogstride     % 

%Display the data 
disp(['The total distance traveled is: ', num2str(totaldis),'miles'])

disp(['You took ', num2str(catsteps) 'steps'])
disp(['You took ', num2str(dogsteps) 'steps'])


% Creating Graphics 
plot(accelTime,Xacc);
hold on; 
plot(accelTime,Yacc);
plot(accelTime,Zacc);
xlim([0 50])
hold off

