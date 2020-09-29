import React, {Component} from "react";
import {Navbar, Nav, Row, Col, Container, NavDropdown, ToggleButton, ButtonGroup, Table} from "react-bootstrap";
import "./styles.css";

class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      teacherName: "[Teacher Name]",
      scopeName: "[World Name]",
      statistics: "Average",
      scope: "World",
    }
  }

  generateTable(){
    return (
      <Table bordered hover>

      </Table>
    )
  }

  render() {
    return (
      <>
      <Navbar bg="dark" variant="dark">
        <Navbar.Brand>Welcome {this.state.teacherName}</Navbar.Brand>
        </Navbar>
        <Container fluid>
          <Row>
            <Col xs="auto">
            <Nav class="col-md-12 d-none d-md-block bg-light sidebar">
                <Nav.Link>
                  Game Statistics
                </Nav.Link>
                <Nav.Link>
                  Manage Player
                </Nav.Link>
                <Nav.Link>
                  Post Question
                </Nav.Link>
                <NavDropdown title="Manage Questions">
                  <NavDropdown.Item>
                    Add
                  </NavDropdown.Item>
                  <NavDropdown.Item>
                    Remove
                  </NavDropdown.Item>
                  <NavDropdown.Item>
                    Approve
                  </NavDropdown.Item>
                </NavDropdown>
          </Nav>
          </Col>
              <Col className="p-5">
              <Row>
                <Col>
                  <ButtonGroup toggle>
                    <ToggleButton type="radio" checked={"Average" === this.state.statistics} onChange={() => this.setState({statistics: "Average"})}>
                      Average
                    </ToggleButton>
                    <ToggleButton type="radio" checked={"Max" === this.state.statistics} onChange={() => this.setState({statistics: "Max"})}>
                      Max
                    </ToggleButton>
                    <ToggleButton type="radio" checked={"Min" === this.state.statistics} onChange={() => this.setState({statistics: "Min"})}>
                      Min
                    </ToggleButton>
                  </ButtonGroup>
                </Col>
                <Col>
                  <ButtonGroup toggle>
                    <ToggleButton type="radio" checked={"World" === this.state.scope} onChange={() => this.setState({scope: "World"})}>
                      World
                    </ToggleButton>
                    <ToggleButton type="radio" checked={"Section" === this.state.scope} onChange={() => this.setState({scope: "Section"})}>
                      Section
                    </ToggleButton>
                    <ToggleButton type="radio" checked={"Level" === this.state.scope} onChange={() => this.setState({scope: "Level"})}>
                      Level
                    </ToggleButton>
                  </ButtonGroup>
                </Col>
              </Row>
              <Row>
                <Col>
                <h1>
                {this.state.scopeName} - {this.state.statistics} Accuracy
                </h1>
                </Col>
              </Row>
              <Row>
                <Col>
                {this.generateTable}
                </Col>
              </Row>
              </Col>
          </Row>
        </Container>
    </>
    )
  }
}
export default App;
