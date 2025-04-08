import pyblish.api
import pyblish.util



def main():
    pyblish.api.register_plugin_path("./plugins")
    plugins = pyblish.api.discover()
    context = pyblish.util.collect(plugins=plugins)
    pyblish.util.validate(context,plugins=plugins)
    
    


if __name__ == "__main__":
    main()