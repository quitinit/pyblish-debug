import pyblish.api
import debugpy
class MyPlugin(pyblish.api.ContextPlugin):
    order = pyblish.api.CollectorOrder
    label = "collector"
    

    def process(self, context):
        print(f"running from {__file__}")
        greeting = "hello world"
        print("creating instance")
        instance = context.create_instance("myInstance", family="myFamily",data={"greeting": greeting})
        instance.data["greeting"] = "hello world"

class HelloWorldValidator(pyblish.api.InstancePlugin):
    order = pyblish.api.ValidatorOrder
    families = ["myFamily"]
    hosts = ["python"]
    label = "validator"

    def process(self, instance):
        print("validating")
        debugpy.breakpoint()
        assert instance.data.get("greeting") == "hello world"
        assert instance.data.get("greeting") == instance.data.get("greeting"), "Greeting is not the same"