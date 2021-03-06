
from google.appengine.ext import db

#### Datastore Classes ####

class App(db.Model):
    number = db.IntegerProperty()
    title = db.StringProperty()
    appId = db.StringProperty()
    heroHeader = db.StringProperty()
    heroCopy = db.TextProperty()
    pdfChapter = db.BooleanProperty(default=True)
    conceptualLink = db.BooleanProperty(default=True)
    manyMold = db.StringProperty()
    version = db.StringProperty(default="1")
    timestamp = db.DateTimeProperty(auto_now=True)
    webTutorial = db.BooleanProperty(default=False)
    webTutorialLink = db.StringProperty()

# for the "Build It" section of a generated app page
class Step(db.Model):
	# appId = db.IntegerProperty() # specifies app the step belongs to
	appId = db.StringProperty() # temporary identifier | TODO: remove this
	number = db.IntegerProperty()
	header = db.StringProperty()
	copy = db.TextProperty()
	videoPath = db.StringProperty()
	fullscreenPath = db.StringProperty()
	timestamp = db.DateTimeProperty(auto_now=True)

class Concept(db.Model):
	# appId = db.IntegerProperty() # specifies app the step belongs to
	appId = db.StringProperty() # temporary identifier | TODO: remove this
	number = db.IntegerProperty()
	header = db.StringProperty()
	copy = db.TextProperty()
	blockPath = db.StringProperty()
	videoPath = db.StringProperty()
	fullscreenPath = db.StringProperty()
	timestamp = db.DateTimeProperty(auto_now=True)

class Custom(db.Model):
	# appId = db.IntegerProperty() # specifies app the step belongs to
	appId = db.StringProperty() # temporary identifier | TODO: remove this
	number = db.IntegerProperty()
	header = db.StringProperty()
	copy = db.TextProperty()
	blockPath = db.StringProperty()
	videoPath = db.StringProperty()
	fullscreenPath = db.StringProperty()
	timestamp = db.DateTimeProperty(auto_now=True)


class Account(db.Model):
        user = db.UserProperty()
        profilePicture = db.BlobProperty()
    	firstName = db.StringProperty(default="")
	lastName = db.StringProperty(default="")
	location = db.StringProperty(default="")
	organization = db.StringProperty(default="")
	ifEducator = db.BooleanProperty(default=False)
	educationLevel = db.StringProperty()
	introductionLink = db.StringProperty()
	timestamp = db.DateTimeProperty(auto_now=True)
	latitude = db.FloatProperty()
	longitude = db.FloatProperty()
	displayName= db.StringProperty()

class DefaultAvatarImage(db.Model):
        title = db.StringProperty()
        picture = db.BlobProperty(default=None)

class Position(db.Model):
        latitude = db.FloatProperty()
	longitude = db.FloatProperty()

class Comment(db.Model):
        submitter = db.ReferenceProperty(collection_name='submitter')
        timestamp = db.DateTimeProperty(auto_now=True)
        content = db.StringProperty()
        appId = db.StringProperty()
        replyFrom = db.ReferenceProperty(collection_name='replyFrom')
        replyTo = db.ReferenceProperty(collection_name='replyTo')
	
class Tutorial(db.Model):
        number = db.IntegerProperty()
        title = db.StringProperty()
        tutorialId = db.StringProperty()
        heroHeader = db.StringProperty()
        heroCopy = db.TextProperty()
        timestamp = db.DateTimeProperty(auto_now=True)

class TutorialStep(db.Model):
	# appId = db.IntegerProperty() # specifies app the step belongs to
	tutorialId = db.StringProperty() # temporary identifier | TODO: remove this
	number = db.IntegerProperty()
	header = db.StringProperty()
	copy = db.TextProperty()
	tutorialLink = db.StringProperty()
	timestamp = db.DateTimeProperty(auto_now=True)

class AdminAccount(db.Model):
        name = db.StringProperty()
        gmail = db.StringProperty()
        password = db.StringProperty()
	


# for the "Conceptualize It" section of a generated app page	
# class Concept(db.Model):	 

# for the "Customize It" section of a generated app page
# class Custom(db.Model):

	
