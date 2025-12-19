from selenium.webdriver.common.by import By

from base_pages.base_class import Base_Class


class Drag_And_Drop_page (Base_Class):
    column_a = "column-a"
    column_b = "column-b"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Selenium’s native ActionChains cannot handle in modern websites. 
    JavaScript HTML5 Drag & Drop Simulation is most reliable. Below is the code"""
    def drop_column(self):
        js_drag_and_drop = """
            function simulateDragDrop(sourceNode, destinationNode) {
                var EVENT_TYPES = {
                    DRAG_END: 'dragend',
                    DRAG_START: 'dragstart',
                    DROP: 'drop'
                }

                function createCustomEvent(type) {
                    var event = new CustomEvent("CustomEvent");
                    event.initCustomEvent(type, true, true, null);
                    event.dataTransfer = {
                        data: {},
                        setData: function(key, value) {
                            this.data[key] = value;
                        },
                        getData: function(key) {
                            return this.data[key];
                        }
                    };
                    return event;
                }

                function dispatchEvent(node, type, event) {
                    if(node.dispatchEvent) {
                        return node.dispatchEvent(event);
                    }
                }

                var dragStartEvent = createCustomEvent(EVENT_TYPES.DRAG_START);
                dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, dragStartEvent);

                var dropEvent = createCustomEvent(EVENT_TYPES.DROP);
                dispatchEvent(destinationNode, EVENT_TYPES.DROP, dropEvent);

                var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END);
                dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent);
            }

            simulateDragDrop(arguments[0], arguments[1]);
        """

        column_a = self.driver.find_element(By.ID, self.column_a)
        column_b = self.driver.find_element(By.ID, self.column_b)
        self.driver.execute_script(js_drag_and_drop, column_a, column_b)
